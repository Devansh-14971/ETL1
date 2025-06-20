import os
import json
import cv2
from pathlib import Path
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QLineEdit
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
from config_ import Config
from AppLogger import Logger
from utils import ensure_directory_exists, save_image, resolve_path


### Show what types of photo types are allowed in the file browse dialog
### Multiple models 
# After building detection, labelled data can be used for training ML.
# Add browse folder for output in the building detection as well as others.for loading as well as saving
# Allow changing of hyperparameters
# Upload checkpoint to process model

class ImageProcessorWorker(QObject):
    progress_updated = pyqtSignal(int)
    file_processed = pyqtSignal(str)
    processing_complete = pyqtSignal(int)
    error_occurred = pyqtSignal(str)

    def __init__(self, config: Config, logger: Logger, save_folder: Path):
        super().__init__()
        self.config = config
        self.logger = logger
        self.is_paused = False
        self.is_cancelled = False
        self.save_folder = save_folder

        self.supported_files = tuple(
            item.strip() for item in self.config.get_allowed_file_types().split(',')
        )

    def _parts_of_img(self, img, dimensions: tuple[int, int] = (100, 100)) -> list:
        x, y = dimensions
        return [img[0:y, 0:x//2], img[0:y, x//2:x]] if x > 0 and y > 0 else []

    def _save_image_with_coords(self, image, save_folder: Path, name, coordinates=(0, 0)):
        save_path = save_folder / f'{name}_{coordinates}.jpg'
        return save_image(image, save_path, logger=self.logger), save_path

    def _get_all_addresses(self) -> list:
        directory = self.config.get_current_input_folder_process()
        if not directory.exists():
            return []
        files = []
        for ext in self.supported_files:
            files.extend(directory.glob(f"*{ext}"))
        return files

    def _process_file(self, image_path: Path) -> dict:
        size_img = self.config.get_image_size()
        if isinstance(size_img, str):
            size_img = tuple(int(i) for i in size_img.split(','))
        blur_region = self.config.get_blur_size()

        image = cv2.imread(str(image_path))
        if image is None:
            return {"source_file": str(image_path), "saved_files": [], "success": False}

        images = self._parts_of_img(image, (size_img[0], size_img[1] - blur_region))

        ensure_directory_exists(self.save_folder)

        saved_files = []
        for x, img in enumerate(images):
            if img is not None:
                success, path = self._save_image_with_coords(img, self.save_folder, name=image_path.stem, coordinates=(0, x))
                if success:
                    saved_files.append(str(path))

        return {
            "source_file": str(image_path),
            "saved_files": saved_files,
            "success": bool(saved_files)
        }

    @pyqtSlot()
    def run(self):
        image_paths = self._get_all_addresses()
        if not image_paths:
            self.error_occurred.emit("No valid image files found.")
            return

        all_metadata = []
        success_count = 0

        metadata_file = self.save_folder / "processed_metadata.json"

        for index, path in enumerate(image_paths):
            while self.is_paused:
                QThread.msleep(100)

            if self.is_cancelled:
                self.logger.log_status("Processing cancelled by user.")
                break

            result = self._process_file(path)
            all_metadata.append(result)

            if result["success"]:
                success_count += 1
                self.file_processed.emit(str(path))

            progress = int(((index + 1) / len(image_paths)) * 100)
            self.progress_updated.emit(progress)

        if not self.is_cancelled:
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(all_metadata, f, indent=4)

            self.config.set_input_folder_detection(str(self.save_folder))
            self.processing_complete.emit(success_count)

class CropWindow(QWidget):
    def __init__(self, config: Config, logger: Logger):
        super().__init__()
        self.config = config
        self.logger = logger
        self.threader = None
        self.worker = None

        self.save_folder = resolve_path("Processed_files")
        
        self.setToolTip("Perform custom image slicing, blurring, or other preprocessing operations before model inference.")
        
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.folder_input = QLineEdit(self)
        self.browse_button = QPushButton("Browse Folder", self)
        self.process_button = QPushButton("Start Processing", self)
        self.status_label = QLabel("Status: Idle", self)

        self.layout.addWidget(self.folder_input)
        self.layout.addWidget(self.browse_button)
        self.layout.addWidget(self.process_button)
        self.layout.addWidget(self.status_label)

        self.setLayout(self.layout)

        self.browse_button.clicked.connect(self.browse_folder)
        self.process_button.clicked.connect(self.start_processing)
    
    @pyqtSlot()
    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.folder_input.setText(folder)
            self.config.set_input_folder_process(folder)

    @pyqtSlot()
    def start_processing(self):
        self.process_button.setEnabled(False)
        self.browse_button.setEnabled(False)
        self.status_label.setText("Status: Processing...")

        self.threader = QThread()
        self.worker = ImageProcessorWorker(self.config, self.logger, self.save_folder)
        self.worker.moveToThread(self.threader)

        self.threader.started.connect(self.worker.run)
        self.worker.progress_updated.connect(self.on_progress)
        self.worker.file_processed.connect(self.on_file_processed)
        self.worker.processing_complete.connect(self.on_processing_complete)
        self.worker.error_occurred.connect(self.on_error)

        self.threader.start()

    def on_progress(self, progress):
        self.status_label.setText(f"Progress: {progress}%")

    def on_file_processed(self, filename):
        self.logger.log_status(f"Processed: {filename}")

    def on_processing_complete(self, count):
        self.status_label.setText(f"Completed! {count} files processed.")
        self.process_button.setEnabled(True)
        self.browse_button.setEnabled(True)

    def on_error(self, message):
        self.status_label.setText(f"Error: {message}")
        self.process_button.setEnabled(True)
        self.browse_button.setEnabled(True)


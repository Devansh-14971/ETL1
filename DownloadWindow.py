from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox
)
from PyQt5.QtCore import Qt
from pathlib import Path
import AppLogger
from config_ import Config
from Downloader import Downloader


class DownloadWindow(QWidget):
    """
    PyQt version of the download trigger UI (not the popup).
    Lets user select folder and initiate download.
    """
    def __init__(self, logger: AppLogger.Logger, config: Config):
        super().__init__()
        self.logger = logger
        self.config = config
        self.folder = self.config.get_current_working_folder()
        self.downloader = None  # Will create when needed

        self.setToolTip("Search and download images from GitHUb's presaved dataset.")

        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle("Download Manager")
        self.setMinimumSize(600, 150)

        layout = QVBoxLayout()

        self.folder_label = QLabel("Destination Folder:")
        self.folder_input = QLineEdit(str(self.folder))
        self.browse_button = QPushButton("Browse")
        self.download_button = QPushButton("Start Download")

        self.browse_button.clicked.connect(self.browse_folder)
        self.download_button.clicked.connect(self.start_download)

        layout.addWidget(self.folder_label)
        layout.addWidget(self.folder_input)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.download_button)

        self.setLayout(layout)

    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.folder_input.setText(folder)
            self.folder = Path(folder)

    def start_download(self):
        selected_path = Path(self.folder_input.text())
        if not selected_path.exists():
            QMessageBox.critical(self, "Invalid Folder", "The selected folder does not exist.")
            return

        self.config.set_save_folder(str(selected_path))
        self.downloader = Downloader(self.logger, self.config)
        self.downloader.exec_()  # Blocking popup
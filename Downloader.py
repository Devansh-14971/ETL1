import os
import requests
from pathlib import Path
from dotenv import load_dotenv
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QProgressBar,
    QTextEdit, QHBoxLayout, QApplication, QMessageBox, QDialog
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal

import AppLogger
from config_ import Config
from utils import resolve_path


class DownloadThread(QThread):
    progress = pyqtSignal(int, int)
    file_downloaded = pyqtSignal(str)
    finished = pyqtSignal()
    error = pyqtSignal(str)
    files_list = pyqtSignal(list)

    def __init__(self, config: Config, logger: AppLogger.Logger):
        super().__init__()
        self.config = config
        self.logger = logger
        self.destination_folder = config.get_current_working_folder()
        self.allowed_extensions = tuple(ext.strip().lower() for ext in config.get_allowed_file_types().split(","))
        self.github_repo = os.getenv("REPO_NAME")
        self.github_username = os.getenv("GITHUB_USERNAME")
        self.github_token = os.getenv("GITHUB_ACCESS_TOKEN")
        self.github_folder = os.getenv("GITHUB_FOLDER_NAME")
        self._cancelled = False

    def cancel(self):
        self._cancelled = True

    def run(self):
        try:
            if not (self.github_username and self.github_repo and self.github_token):
                self.error.emit("GitHub credentials missing.")
                return

            if not self.destination_folder.exists():
                self.logger.log_warning("Destination folder does not exist.")
                return

            files = self._fetch_file_list()
            filtered_files = [
                file for file in files
                if file["type"] == "file" and file["name"].lower().endswith(self.allowed_extensions)
            ]

            self.files_list.emit(filtered_files)

            total_files = len(filtered_files)
            for i, file in enumerate(filtered_files, 1):
                if self._cancelled:
                    self.logger.log_status("Download cancelled.")
                    break
                self._download_file(file["download_url"], file["name"])
                self.progress.emit(i, total_files)

            self.finished.emit()

        except requests.RequestException as e:
            self.error.emit(str(e))

    def _fetch_file_list(self):
        url = f"https://api.github.com/repos/{self.github_username}/{self.github_repo}/contents/{self.github_folder}/"
        headers = {"Authorization": f"token {self.github_token}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def _download_file(self, url, filename):
        response = requests.get(url, stream=True)
        response.raise_for_status()
        filepath = self.destination_folder / filename
        with open(filepath, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        self.file_downloaded.emit(filename)


class Downloader(QDialog):
    def __init__(self, logger: AppLogger.Logger, config: Config):
        super().__init__()
        self.logger = logger
        self.config = config
        self.threader = DownloadThread(config, logger)
        load_dotenv(resolve_path("secrets.env"))
        self.setWindowTitle("Download Files")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.progress_bar = QProgressBar()
        self.progress_label = QLabel("Progress: 0%")

        self.found_files_text = QTextEdit()
        self.found_files_text.setReadOnly(True)
        self.downloaded_files_text = QTextEdit()
        self.downloaded_files_text.setReadOnly(True)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.cancel_download)

        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close_dialog)
        self.close_button.setEnabled(False)

        layout.addWidget(self.progress_bar)
        layout.addWidget(self.progress_label)

        text_layout = QHBoxLayout()
        text_layout.addWidget(self.found_files_text)
        text_layout.addWidget(self.downloaded_files_text)
        layout.addLayout(text_layout)

        layout.addWidget(self.cancel_button)
        layout.addWidget(self.close_button)
        self.setLayout(layout)

        self.threader.progress.connect(self.update_progress)
        self.threader.file_downloaded.connect(self.add_downloaded_file)
        self.threader.finished.connect(self.on_finished)
        self.threader.error.connect(self.show_error)
        self.threader.files_list.connect(self.display_files_found)

        self.threader.start()

    def update_progress(self, current, total):
        percent = int((current / total) * 100)
        self.progress_bar.setValue(percent)
        self.progress_label.setText(f"Progress: {percent}%")

    def display_files_found(self, files):
        self.found_files_text.append("Files Found:")
        for file in files:
            self.found_files_text.append(file['name'])

    def add_downloaded_file(self, filename):
        self.downloaded_files_text.append(f"Downloaded: {filename}")

    def cancel_download(self):
        self.threader.cancel()
        self.cancel_button.setEnabled(False)
        self.logger.log_status("Download cancellation requested.")

    def on_finished(self):
        self.close_button.setEnabled(True)
        self.cancel_button.setEnabled(False)
        QMessageBox.information(self, "Done", "Download completed or cancelled.")

    def show_error(self, message):
        QMessageBox.critical(self, "Error", message)
        self.close_button.setEnabled(True)
        self.cancel_button.setEnabled(False)

    def close_dialog(self) -> None:
        self.close()

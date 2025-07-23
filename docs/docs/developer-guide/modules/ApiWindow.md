# ApiWindow.py

## Purpose
This Module implements the 'Downloading images from a map' functionality. 

## Used By
- `main_app.py` as a tab in a `QTabWidget` embedded in the main window. 
-- {insert screenshot of API Window here} 

## Key Classes

---

### `CoordinateReceiver`
- **Inherits**: QObject
- **Inputs**: _None, Uses pyqtSignal class 'coordinatesRecieved(object)' to accept signals_
- **Role**: _Facilitates usage of coordinates independently of the code currently running_ 

#### Methods

##### `receiveCoordinates(coords)`
- **Inputs**: coords
- **Function**: _Emits `coordinatesRecieved(QVariant)` so that other functions listening for it can accept the coords_
- **Output**: _None_

---

### `StreetViewDownloader`
- **Inputs**: (output_dir, max_images, logger, config, FOUND_COORDS)
- **pyqtSignals used**: `progress(int,int)` and `finished`
- **Triggers on `__init__`**: _Initializes all variables required by the helper functions_

    _Initializes the following variables_
```
    self.coords
    self.api_key
    self.config
    self.region
    self.output_dir
    self.max_images
    self.logger 
```

#### Methods

##### `run()`
- **Inputs**: None
- **Function**: _Leverages the `self.coords` and `download_panorama` function to request for and download StreetView images. Is used by`self.coord_reciever` and connected to `self.oncoordinates(coords)` function _

_Recieves coordinateRecieved signal that contains a JSON type `coords` variable and _ 
    _Updates `self.progress` and has exception handling_ 
- **Output**: _emits the `self.finished` pyqtSignal when done_

---

### `ApiWindow`
- **Inherits**: `QWidget`
- **Inputs**: (logger, config)
- **Initializes on `__init__`**: _Initializes all variables required by helper functions_
    _Initializes the following variables_
    ```
    self.logger
    self.config
    self.secrets_path
    self.DB_PATH
    self.FOUND_COORDS
    self.region
    self.output_dir
    ```

- **Triggers on `__init__`**:
    
    _Triggers `QTimer.singleshot(0, lambda: self.set_api_key(self.secrets_path))`_

    _Triggers `self.setup_ui()`_

#### Methods

##### `set_api_key(path)`
- **Inputs**: path: Path
- **Function**: 

    -_Sets up a QInputDialog class `dialog` variable. Size of window is set as `(400,100)`_

    -_Centers the window according to the main_window_

    -_If an api_key is submitted, writes the `api_key` to file given in `path`_

    -_Initializes environmental variable by using `load_dotenv`_

    -_Triggers `self.setup_map`_

##### `setup_ui()`
- **Inputs**: None
- **Output**: _Sets up the UI interface for `Download` tab_
- **Function**: 

    -_Sets up `self.layout` as a `QVBoxLayout(self)`_

    -_Sets up `top_layout` as a `QHBoxLayout()`_
    -_Sets up `self.city_dropdown` as a `QComboBox` that has minimum width set to 200. Added to `top_layout` with `QLabel` 'City'_

    -_Sets up two buttons `self.rect_btn` and `self.clear_btn` as `QPushButton`. Both are added to top_layout_

    -_Triggers `self.populate_city_dropdown()`_

    -_Connects `self.on_city_celected()` to `city_dropdown`'s `.currentIndexChanged`_

    -_Sets up `self.spin_label` as a `QLabel` and `self.spin` as a `QSpinBox`. `self.spin` has a range of 0 to 10,000._

---

!!! danger "`self.spin` has a usage limit"

    Don't set this to more than `10,000` — Google's Street View API has a free tier limit of 10,000 images.  
    Modifying this may lead to unexpected billing or failed downloads.

---
-
    -_Adds `self.spin_label` and `self.spin` to `top_layout`_

    -_Sets up `self.folder_btn` as a `QPushButton` and self.folder_label as a `QLabel`_
    
    -_Adds `self.folder_btn` and `self.folder_label` to `top_layout`_

    -_Sets up `self.download_btn` as a `QPushButton` and adds this to `top_layout`_

    -_Adds `top_layout` to `self.layout`_

    -_Sets up `self.view` as a `QWebEngineView` to create an area to display the map. Is added to `self.layout`_

    -_Sets up a progress bar(`QProgressBar`) as `self.progress`. Is added to `self.layout`_

    -_Connects `self.run_js('enableRectangle())` to `self.rect_btn`'s `.clicked`_

    -_Connects `self.run_js('clearSelection())` to `self.clear_btn`'s `.clicked`_

    -_Connects `self.choose_folder()` to `self.folder_btn`'s `.clicked`_

    -_Connects `self.start_download()` to `self.download_btn`'s `.clicked`_


##### `query_results(db_path, north, south, east, west)`
- **Inputs**: db_path, north, south, east, west
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `setup_map()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `run_js(script)`
- **Inputs**: script
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `choose_folder()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `on_coordinates(coords)`
- **Inputs**: coords
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `start_download()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `update_progress(current, total)`
- **Inputs**: current, total
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._


## Imports
_TODO: List meaningful imports._

## Notes / Caveats
```
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QProgressBar, QLabel, QSpinBox, QInputDialog, QComboBox, QMessageBox)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QColor
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QThread, QTimer, Qt
from AppLogger import Logger
import json
from config_ import Config
import requests
import os, json
import sqlite3
from Tile_Downloader import download_panorama
from dotenv import load_dotenv
from utils import resolve_path
from pathlib import Path
from Metadata_scanner_grid_search import StreetViewDensityScanner
```

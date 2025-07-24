# ApiWindow.py

## Purpose
This Module implements the 'Downloading images from a map' functionality. 

## Used By
- `~/main_app.py` as a tab in a `QTabWidget` embedded in the main window. 
-- {insert screenshot of API Window here} 

## Key Classes

---

### `CoordinateReceiver`
- **Inherits**: QObject
- **Inputs**: _None, Uses pyqtSignal class `coordinatesRecieved(object)` to accept signals_
- **Role**: _Facilitates usage of coordinates independently of the code currently running_ 

#### Methods

##### `receiveCoordinates(coords)`
- **Inputs**: coords: JSON-like
- **Output**: _None_
- **Detailed_Function**: _Emits `coordinatesRecieved(QVariant)` so that other functions listening for it can accept the coords_

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
- **Output**: _emits the `self.finished` pyqtSignal when done_
- **Detailed_Function**: _Leverages the `self.coords` and `download_panorama()` function to request for and download StreetView images. Is used by`self.coord_reciever` and connected to `self.oncoordinates(coords)` function _

_Recieves coordinateRecieved signal that contains a JSON type `coords` variable and _ 
    _Updates `self.progress` and has exception handling_ 

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
- **Output**: _Sets API key by prompting the user_
- **Detailed_Function**: 

    - _Sets up a QInputDialog class `dialog` variable. Size of window is set as `(400,100)`_

    - _Centers the window according to the main_window_

    - _If an api_key is submitted, writes the `api_key` to file given in `path`_

    - _Initializes environmental variable by using `load_dotenv()`_

    - _Triggers `self.setup_map()`_

##### `setup_ui()`
- **Inputs**: None
- **Output**: _Sets up the UI interface for `Download` tab_
- **Detailed_Function**: 

    - _Sets up `self.layout` as a `QVBoxLayout(self)`_

    - _Sets up `top_layout` as a `QHBoxLayout()`_
    - _Sets up `self.city_dropdown` as a `QComboBox` that has minimum width set to 200. Added to `top_layout` with `QLabel` 'City'_

    - _Sets up two buttons `self.rect_btn` and `self.clear_btn` as `QPushButton`. Both are added to top_layout_

    - _Triggers `self.populate_city_dropdown()`_

    - _Connects `self.on_city_celected()` to `city_dropdown`'s `.currentIndexChanged`_

    - _Sets up `self.spin_label` as a `QLabel` and `self.spin` as a `QSpinBox`. `self.spin` has a range of 0 to 10,000._

---

!!! danger "`self.spin` has a usage limit"

    Don't set this to more than `10,000` — Google's Street View API has a free tier limit of 10,000 images.  
    Modifying this may lead to unexpected billing or failed downloads.

---
-   - _Adds `self.spin_label` and `self.spin` to `top_layout`_

    - _Sets up `self.folder_btn` as a `QPushButton` and self.folder_label as a `QLabel`_
    
    - _Adds `self.folder_btn` and `self.folder_label` to `top_layout`_

    - _Sets up `self.download_btn` as a `QPushButton` and adds this to `top_layout`_

    - _Adds `top_layout` to `self.layout`_

    - _Sets up `self.view` as a `QWebEngineView` to create an area to display the map. Is added to `self.layout`_

    - _Sets up a progress bar(`QProgressBar`) as `self.progress`. Is added to `self.layout`_

    - _Connects `self.run_js('enableRectangle())` to `self.rect_btn`'s `.clicked`_

    - _Connects `self.run_js('clearSelection())` to `self.clear_btn`'s `.clicked`_

    - _Connects `self.choose_folder()` to `self.folder_btn`'s `.clicked`_

    - _Connects `self.start_download()` to `self.download_btn`'s `.clicked`_

##### `populate_city_dropdown()`
- **Inputs**: None  
- **Output**: _Populates the city dropdown with all city names in `cities.txt`, colors available ones green and unavailable ones red._  
- **Detailed_Function**:  
    - _Clears `self.city_dropdown` and initializes `self.city_color_map` as an empty dict._  
    - _Loads `city_map_data` from the JSON file at the path from `config.get_map_index_path()`._  
    - _Creates `available_maps` by scanning filenames in the `Metadata_Maps` folder and checking for `.html` files._  
    - _Reads `cities.txt`, strips whitespace, and stores city names._  
    - _For each city, adds it to `self.city_dropdown`, sets the dropdown text color based on availability, and updates `self.city_color_map`._  
    - _If current `self.region` matches a city name, selects it in the dropdown._

##### `on_city_selected()`
- **Inputs**: None  
- **Output**: _Prompts for metadata if city not available, launches `StreetViewDensityScanner`, and updates the map._  
- **Detailed_Function**:  
    - _Fetches and formats the selected city from the dropdown._  
    - _If no metadata is found (based on `self.city_color_map`), prompts the user to fetch/generate it._  
    - _If agreed, tries to load bounds from `city_map_data`. If not found, calls `fetch_city_bounds()`._  
    - _If successful, updates `map_index.json` and repopulates the dropdown._  
    - _Initializes `StreetViewDensityScanner`, pre-fills form fields, and starts scanning._  
    - _Sets `self.region` to the selected city and calls `setup_map()`._

##### `fetch_city_bounds(city)`
- **Inputs**: `city: str`  
- **Output**: _Returns bounds of the city as a dictionary with `north`, `south`, `east`, `west` keys_  
- **Detailed_Function**:  
    - _Sends a GET request to Nominatim’s public API for the city’s bounding box._  
!!! warning "Hard Code present in function"
_The `headers` dictionary was hard coded as it was thought to be not important enough to properly add custom functions to `config_.py`_
-    - _Extracts bounding box (`bbox`) values from JSON response._  
     - _Converts these values into a float dictionary of bounds._  
     - _Returns the `bounds` dictionary. If an error occurs, logs the exception and returns None._

##### `update_map_index(city, bounds)`
- **Inputs**: `city: str`, `bounds: dict`  
- **Output**: _Updates `map_index.json` with new bounds for the city_  
- **Detailed_Function**:  
    - _Reads existing data from `map_index.json` if it exists._  
    - _Adds/updates the city’s bounds in lowercase format._  
    - _Overwrites `map_index.json` with the new content._  
    - _Logs success or failure._

##### `query_results(db_path, north, south, east, west)`
- **Inputs**: `db_path`, `north`, `south`, `east`, `west`  
- **Output**: _Returns a list of `(lat, lon, pano_id)` tuples from the DB that fall inside the given bounds_  
- **Detailed_Function**:  
    - _Connects to SQLite database at `db_path`._  
    - _Runs a SQL query on `coords` and `results` tables, selecting coordinates that lie inside the bounding box._  
    - _Fetches and returns results._  
    - _Closes connection and logs the result._

##### `setup_map()`
- **Inputs**: None  
- **Output**: _Initializes and embeds a Google Maps HTML page in `self.view`, sets up JS-QWebChannel communication_  
- **Detailed_Function**:  
    - _Reads API key from environment._  
    - _Instantiates `QWebChannel` and `CoordinateReceiver`, connects signal to `on_coordinates()`._  
    - _Registers JS receiver in the channel and sets it on the `QWebEngineView` page._  
    - _Loads the map center and bounds from the selected `self.region`._  
    - _Constructs and embeds a Google Maps HTML page with JS drawing tools_  
    - _Defines JavaScript hooks to draw and send rectangle/circle/polygon coordinates to Python._  
    - _Displays this map in `self.view`._  
    - _Logs success._

##### `run_js(script)`
- **Inputs**: `script: str`  
- **Output**: _Runs the passed JavaScript code in the embedded web page_  
- **Detailed_Function**:  
    - _Passes the `script` to `self.view.page().runJavaScript()`._  
    - _Logs the JS execution attempt._  
    - _Catches and logs any exceptions if JS execution fails._

##### `choose_folder()`
- **Inputs**: None  
- **Output**: _Sets `self.output_dir` and updates folder label with selected path._  
- **Detailed_Function**:  
    - _Opens a directory selection dialog using `QFileDialog.getExistingDirectory()`._  
    - _If the user selects a valid folder, updates `self.output_dir` and updates the label._  
    - _Logs the selected folder or logs an error on failure._

##### `on_coordinates(coords)`
- **Inputs**: `coords: list`  
- **Output**: _Stores selected shape's coordinates and fetches matching coordinates from DB._  
- **Detailed_Function**:  
    - _Logs the received shape coordinates from JS._  
    - _Parses `north`, `south`, `east`, `west` from `coords` assuming a rectangle._  
    - _Uses `query_results()` to fetch DB results inside bounds._  
    - _Appends the results to `self.FOUND_COORDS`._  
    - _Logs the number of found coordinates._  
    - _Saves `coords` to `self.current_shape_coords`._

##### `start_download()`
- **Inputs**: None  
- **Output**: _Starts the `StreetViewDownloader` thread to begin image download_  
- **Detailed_Function**:  
    - _Validates that `self.current_shape_coords` is present._  
    - _Fetches maximum image count from spin box._  
    - _Validates that `self.output_dir` is set._  
    - _Initializes a `StreetViewDownloader` thread with selected region, output folder, and coordinates._  
    - _Connects the thread's signals (`progress`, `finished`) to update progress bar and log completion._  
    - _Sets the progress bar's max value and starts the thread._  
    - _Catches and logs any exceptions._

##### `update_progress(current, total)`
- **Inputs**: current, total
- **Detailed_Function**: _Helper function thhat updates progress_

<!-- Older -->

##### `populate_city_dropdown()`
- **Inputs**: None
- **Output**: _Populates the city dropdown with all city names in `cities.txt`_
- **Detailed_Function**:


##### `on_city_selected()`
- **Inputs**: None
- **Output**: _Throws a user prompt if the selected city's metadata is not available in the database. If the users responds positively, the `StreetViewDensityScanner(city)` is triggered. Finally, it sets up the map_
- **Detailed_Function**:

##### `fetch_city_bounds(city)`
- **Inputs**: city: str
- **Output**: _Returns `bounds {dict[float]}` of the `city` requested via `nominatim`_

- **Detailed_Function**:

##### `update_map_index(city, bounds)`
- **Inputs**: city: str, bounds: dict
- **Output**: _Updates `~/map_index.json` with the newly acquired `bounds` of the `city`_
- **Detailed_Function**:

##### `query_results(db_path, north, south, east, west)`
- **Inputs**: db_path, north, south, east, west
- **Output**: _Returns coordinates as `results {List}`_
- **Detailed_Function**: __

##### `setup_map()`
- **Inputs**: None
- **Output**: _Sets up the map_
- **Detailed_Function**: _TODO: What this does._

##### `run_js(script)`
- **Inputs**: script
- **Output**: _Runs Javascript `script` with `.runJavaScript()`_
- **Detailed_Function**: _TODO: What this does._

##### `choose_folder()`
- **Inputs**: None
- **Detailed_Function**: _Sets self.output_dir to `folder` retrieved via `QFileDialog.getExistingDirectory()`_

##### `on_coordinates(coords)`
- **Inputs**: coords
- **Output**: _Sets `self.current_shape_coords` to `coords` and appends to `self.FOUND_COORDS`_
- **Detailed_Function**: _TODO: What this does._

##### `start_download()`
- **Inputs**: None
- **Output**: _Starts `StreetViewDownloader`_
- **Detailed_Function**: _TODO: What this does._


## Imports
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

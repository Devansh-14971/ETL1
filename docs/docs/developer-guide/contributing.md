# Contributing to This Project

Thanks for your interest in contributing! Whether you're fixing bugs, improving documentation, or adding features — you're very welcome here. 

Please follow the steps below to help keep the project consistent and stable.

---

## Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```
2. **(Optional) Create a virtual environment**
    ```
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```
3. **Install dependencies**
    ```
    pip install -r requirements.txt
    ```

4. **Run the app**
    ```
    python main_app.py
    ```
    OR
    ```
    py main_app.py
    ```

## Project Structure (Short Overview)


```python
/main_app.py                  # Entry point of the app
/ApiWindow.py                 # UI logic for map/street view download
/AppLogger.py                 # Custom logging logic for status updates
/BuildingDetection.py         # Core building detection logic
/BuildingDetectionWindow.py   # UI for building detection configuration
/Classification.py            # Image classification utilities
/config_.py                   # Custom module to interface with configuration file 
/config_.ini                  # Configurations and constants used throughout
/CropStreetWindow.py          # UI to crop Google StreetView sourced images
/Duplicates_Better.py         # Duplicate detection and filtering
/geoscatter.py                # For scatter-plotting map points
/map_index_maker.py           # Generates indexes for grid-based mapping
/Metadata_scanner_grid_search.py # Grid scanning of image metadata over map
/model_download.py            # Downloads pre-trained models
/model_training.py            # Training routines for new models
/Tile_Downloader.py           # Handles downloading map tiles
/utils.py                     # Common utility functions used everywhere
```


## Submitting a Change

### Create a branch
```
git checkout -b fix/your-issue-name
```

### Make your changes
- Add meaningful commit messages.

- Keep the code style consistent with the rest of the codebase.

### Test your code

- Make sure the app runs and your change doesn't break anything.

### Submit a Pull Request

- Go to GitHub, open a PR into main.

- Explain the what and why of your change.

- Link any related issues, if applicable.

### Good Practices

- Comment your code where logic is complex.

- Add docstrings for new functions and classes.

- Update documentation if your change affects behavior or UI.

- Be kind and constructive in communication!

### Code Style & Formatting
- Python 3.10+
 
- Follow PEP8
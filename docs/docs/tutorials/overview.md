# Main Application Overview (`main_app.py`)

This module serves as the **entry point** and central coordinator for the PyQt5-based GUI application. It handles the layout, top-level tab management, sidebar functions, and the first-time setup of dependencies like models and map indexes.

---

## Purpose

- Launch and manage the entire GUI.
- Initialize config, model, and map index on first run.
- Register and display all feature windows (tabs).
- Handle user interactions like showing logs, editing configuration, and model registration.

---

## High-Level Structure

```python
/main_app.py
    /OverlaySidebar         # Sidebar UI with buttons for logs, config, models, and map view
    /MainApp (QMainWindow)  # Main window with tab management and topbar
        /add_tab(...)       # Adds each feature module as a tab
        /show_logs(...)     # Displays the log viewer
        /show_config(...)   # Opens editable config in a scrollable dialog
        /add_model_form(...)# Opens form to add new model via URL and metadata
        /show_geoscatter()  # Displays geospatial plot image
    /__main__               # Bootstraps the app using QApplication
```
## Sidebar Buttons (OverlaySidebar)
*Accessible via the ☰ burger menu, contains:*

- Show Logs: Opens a window with the contents of the app's log file.

- Show Config: Opens a dialog where users can edit settings stored in config_.ini.

- Add Model: Lets the user input a model URL and name to register a new classifier.

- Show Geoscatter: Opens a pre-generated scatter plot image from the geospatial analysis module.

## First-Time Setup Logic

- Downloads the default model using model_download.py if not already present.

- Generates the map index using map_index_maker.py if missing.

- Loads settings from config_.ini using the custom config_ module.

## Notes

- Tab classes like ApiWindow, CropWindow, etc., are imported lazily and constructed at runtime with config and logger passed in.

- config_.py and AppLogger.py are required dependencies.

- main_app.py is designed to run via `python main_app.py` and should not be imported as a module.
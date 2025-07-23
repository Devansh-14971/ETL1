## module_name.py

**Purpose:** Handles X logic.

**Used by:** main.py, gui/feature1.py

### Key Classes/Functions:
- `ImageProcessor`: Applies filters and returns result
- `load_model()`: Loads the ML model from disk

### Notes:
- Uses multiprocessing to avoid UI freeze
- Needs model in `/models/`
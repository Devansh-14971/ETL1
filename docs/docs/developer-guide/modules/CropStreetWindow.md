# CropStreetWindow.py

## Purpose
_TODO: Describe what this module does._

## Used By
- _TODO: List dependent files._

## Key Classes

---

### `ImageProcessorWorker`
- **Inputs**: (config, logger, save_folder)
- **Triggers on `__init__`**: _TODO: Describe what happens._
- **Role**: _TODO: What this class does._

#### Methods

##### `_parts_of_img(img, dimensions)`
- **Inputs**: img, dimensions
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `_save_image_with_coords(image, save_folder, name, coordinates)`
- **Inputs**: image, save_folder, name, coordinates
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `_get_all_addresses()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `_process_file(image_path)`
- **Inputs**: image_path
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `run()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

---

### `CropWindow`
- **Inputs**: (config, logger)
- **Triggers on `__init__`**: _TODO: Describe what happens._
- **Role**: _TODO: What this class does._

#### Methods

##### `init_ui()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `browse_folder()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `start_processing()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `on_progress(progress)`
- **Inputs**: progress
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `on_file_processed(filename)`
- **Inputs**: filename
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `on_processing_complete(count)`
- **Inputs**: count
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `on_error(message)`
- **Inputs**: message
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._


## Imports
_TODO: List meaningful imports._

## Notes / Caveats
_TODO: Any special logic or bugs to be aware of._

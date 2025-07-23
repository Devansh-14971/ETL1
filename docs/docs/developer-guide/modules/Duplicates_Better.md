# Duplicates_Better.py

## Purpose
_TODO: Describe what this module does._

## Used By
- _TODO: List dependent files._

## Key Classes

---

### `DuplicateClassifier`
- **Inputs**: (config, logger, folder)
- **Triggers on `__init__`**: _TODO: Describe what happens._
- **Role**: _TODO: What this class does._

#### Methods

##### `load_model()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `_load_and_preprocess_image(img_path)`
- **Inputs**: img_path
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `_extract_features(images)`
- **Inputs**: images
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `_cluster_features(features)`
- **Inputs**: features
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `_assign_color(class_id)`
- **Inputs**: class_id
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `_save_classified_locations(folder_path, clusters)`
- **Inputs**: folder_path, clusters
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `process_folder(folder_path, progress_callback)`
- **Inputs**: folder_path, progress_callback
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `process_multiple_folders(folder_paths, progress_callback)`
- **Inputs**: folder_paths, progress_callback
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

---

### `DuplicateModelLoaderThread`
- **Inputs**: (config, logger, folder)
- **Triggers on `__init__`**: _TODO: Describe what happens._
- **Role**: _TODO: What this class does._

#### Methods

##### `run()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

---

### `DuplicatesWorker`
- **Inputs**: (config, logger, remove_dir, folder)
- **Triggers on `__init__`**: _TODO: Describe what happens._
- **Role**: _TODO: What this class does._

#### Methods

##### `run()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `pause()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `resume()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `cancel()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

---

### `DuplicatesWindow`
- **Inputs**: (config, logger)
- **Triggers on `__init__`**: _TODO: Describe what happens._
- **Role**: _TODO: What this class does._

#### Methods

##### `init_ui()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `choose_folder()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `on_model_loaded()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `on_model_failed(error)`
- **Inputs**: error
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `start_process()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `update_timer(seconds)`
- **Inputs**: seconds
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `processing_done(seconds)`
- **Inputs**: seconds
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `log_error(msg)`
- **Inputs**: msg
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `pause_process()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `resume_process()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `cancel_process()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._


## Imports
_TODO: List meaningful imports._

## Notes / Caveats
_TODO: Any special logic or bugs to be aware of._

# Classification.py

## Purpose
_TODO: Describe what this module does._

## Used By
- _TODO: List dependent files._

## Key Classes

---

### `Classify`
- **Inputs**: (config, logger, model_dir, num_classes, device)
- **Triggers on `__init__`**: _TODO: Describe what happens._
- **Role**: _TODO: What this class does._

#### Methods

##### `instantiate_model()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `make_folders()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `save_image(image_path, filename, class_)`
- **Inputs**: image_path, filename, class_
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `predict_image(image_path)`
- **Inputs**: image_path
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `organize_images(check_value, output_file_path, progress_callback, labels, selected_model)`
- **Inputs**: check_value, output_file_path, progress_callback, labels, selected_model
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

---

### `ModelLoaderThread`
- **Inputs**: (processor, model_path)
- **Triggers on `__init__`**: _TODO: Describe what happens._
- **Role**: _TODO: What this class does._

#### Methods

##### `run()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

---

### `_ClassificationWorker`
- **Inputs**: (processor, check_value, selected_model, labels, output_folder)
- **Triggers on `__init__`**: _TODO: Describe what happens._
- **Role**: _TODO: What this class does._

#### Methods

##### `run()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

---

### `_ClassificationTimer`
- **Inputs**: ()
- **Triggers on `__init__`**: _TODO: Describe what happens._
- **Role**: _TODO: What this class does._

#### Methods

##### `run()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

---

### `ClassificationWindow`
- **Inputs**: (config, logger)
- **Triggers on `__init__`**: _TODO: Describe what happens._
- **Role**: _TODO: What this class does._

#### Methods

##### `on_model_loaded(model, processor)`
- **Inputs**: model, processor
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `on_model_failed(error)`
- **Inputs**: error
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `init_ui()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `add_class_labels(model_name)`
- **Inputs**: model_name
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `on_select(text)`
- **Inputs**: text
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `browse_folder()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `start_process()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `update_progress(value)`
- **Inputs**: value
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `log_to_output(message)`
- **Inputs**: message
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `on_process_done(location_file_path)`
- **Inputs**: location_file_path
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._


## Imports
_TODO: List meaningful imports._

## Notes / Caveats
_TODO: Any special logic or bugs to be aware of._

# BuildingDetectionWindow.py

## Purpose
_TODO: Describe what this module does._

## Used By
- _TODO: List dependent files._

## Key Classes

---

### `_DetectionWorker`
- **Inputs**: (processor, remove_after)
- **Triggers on `__init__`**: _TODO: Describe what happens._
- **Role**: _TODO: What this class does._

#### Methods

##### `_emit_progress(pct)`
- **Inputs**: pct
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `_emit_log(msg)`
- **Inputs**: msg
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `_emit_image_saved(path)`
- **Inputs**: path
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `run()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

---

### `_DetectionTimer`
- **Inputs**: ()
- **Triggers on `__init__`**: _TODO: Describe what happens._
- **Role**: _TODO: What this class does._

#### Methods

##### `run()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `stop()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

---

### `BuildingDetectionWindow`
- **Inputs**: (config, logger)
- **Triggers on `__init__`**: _TODO: Describe what happens._
- **Role**: _TODO: What this class does._

#### Methods

##### `init_ui()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `_update_process_button_state()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `choose_input_folder()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `choose_model_dir()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `choose_output_folder()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `reset_to_defaults()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `on_process_clicked()`
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

##### `on_process_done()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._


## Imports
_TODO: List meaningful imports._

## Notes / Caveats
_TODO: Any special logic or bugs to be aware of._

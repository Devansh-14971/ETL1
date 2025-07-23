# config_.py

## Purpose
_TODO: Describe what this module does._

## Used By
- _TODO: List dependent files._

## Key Classes

---

### `Config`
- **Inputs**: (logger, path)
- **Triggers on `__init__`**: _TODO: Describe what happens._
- **Role**: _TODO: What this class does._

#### Methods

##### `create_default_config()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `save_config(configfile)`
- **Inputs**: configfile
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `read_config()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get(section, option, fallback)`
- **Inputs**: section, option, fallback
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_all(section)`
- **Inputs**: section
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `set(section, option, value)`
- **Inputs**: section, option, value
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_log_file()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_general_data()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_paths_data()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_download_data()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_building_detection_data()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_duplicates_data()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_classification_data()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_processed_data()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_model_training_data()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_building_detection_recommended()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `set_building_detection_param(option, value)`
- **Inputs**: option, value
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_bd_model_path()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_bd_target_classes()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_bd_input_dir()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_bd_output_dir()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_bd_threshold()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_bd_expand_factor()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_bd_min_dim()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_map_index_path()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_database_path()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_current_working_folder()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_allowed_file_types()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_image_size()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_blur_size()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_model_save_folder()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_target_classes()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_foldr_names_classif()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_classif_folder_name()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_img_ext()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_input_folder_dup()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_current_input_folder_class()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_current_input_folder_process()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_model_file_path()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_model_data()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `get_dwnd_file_path()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `set_model_data(new_data)`
- **Inputs**: new_data
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `set_save_folder(folder)`
- **Inputs**: folder
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `set_input_folder_process(folder)`
- **Inputs**: folder
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `set_input_folder_detection(folder)`
- **Inputs**: folder
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._


## Imports
_TODO: List meaningful imports._

## Notes / Caveats
_TODO: Any special logic or bugs to be aware of._

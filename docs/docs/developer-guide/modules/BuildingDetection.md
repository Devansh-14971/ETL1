# BuildingDetection.py

## Purpose
_TODO: Describe what this module does._

## Used By
- _TODO: List dependent files._

## Key Classes

---

### `ObjectDetectionProcessor`
- **Inputs**: (config, logger)
- **Triggers on `__init__`**: _TODO: Describe what happens._
- **Role**: _TODO: What this class does._

#### Methods

##### `_load_settings()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `_load_detector()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `_expand_box(box, img_width, img_height)`
- **Inputs**: box, img_width, img_height
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `crop_and_save(image, box, save_path)`
- **Inputs**: image, box, save_path
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `calculate_iou(box1, box2)`
- **Inputs**: box1, box2
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `_deduplicate_boxes(boxes, scores, classes)`
- **Inputs**: boxes, scores, classes
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `_read_and_prepare_image(image_path)`
- **Inputs**: image_path
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._

##### `process()`
- **Inputs**: None
- **Function**: _TODO: What this does._
- **Output**: _TODO: Description + type._


## Imports
_TODO: List meaningful imports._

## Notes / Caveats
_TODO: Any special logic or bugs to be aware of._

import os
import requests
import tarfile
from config_ import Config
from AppLogger import Logger

def download_model(logger: Logger, config: Config, model_name = 'faster_rcnn'):

    MODEL_DIR = config.get_model_save_folder()
    model_data = config.get_model_data()
    MODEL_URL = model_data[model_name]['url']

    #MODEL_DIR, MODEL_URL = config.get_model_dwld()
    print(MODEL_DIR)
    os.makedirs(MODEL_DIR, exist_ok=True)
    MODEL_PATH = os.path.join(MODEL_DIR, "model.tar.gz")
    logger.log_status(f"Downloading model from {MODEL_URL} to {MODEL_PATH}...")
    
    response = requests.get(MODEL_URL, stream=True)
    
    if response.status_code == 200:
        with open(MODEL_PATH, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        logger.log_status("Download complete.")
    else:
        logger.log_exception(f"Failed to download. HTTP Status Code: {response.status_code}")
        return

    # Extract model
    logger.log_status("Extracting model...")
    try:
        with tarfile.open(MODEL_PATH, "r:gz") as tar:
            tar.extractall(MODEL_DIR)
        logger.log_status(f"Model extracted successfully to {os.path.abspath('.') + MODEL_DIR}.")
    except Exception as e:
        logger.log_exception(f"An exception occured while extracting model: {e}")

import json
import logging
import os

logger = logging.getLogger(__name__)

def save_data_to_json(data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        logger.info(f"Data written to '{filename}'.")
    except Exception as e:
        logger.error(f"Error saving to '{filename}': {e}")

def load_json_data(filename):
    if os.path.isfile(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading '{filename}': {e}")
    return {}

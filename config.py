import os
import json
import importlib.util

def load_sensitive_info():
    key_path = os.path.join(os.path.dirname(__file__), 'key_dev.py')
    spec = importlib.util.spec_from_file_location("key", key_path)
    key = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(key)
    return {
        "SERVER_ID": key.SERVER_ID,
        "API_KEY": key.API_KEY,
        "BOT_TOKEN": key.BOT_TOKEN
    }

sensitive_info = load_sensitive_info()

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"Configuration file not found at {config_path}.")
    with open(config_path, 'r') as f:
        return json.load(f)

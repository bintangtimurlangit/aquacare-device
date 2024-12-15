import json
import os

STORAGE_FILE = "device_config.json"

def save_device_config(device_id):
    config = {
        "device_id": device_id
    }
    with open(STORAGE_FILE, 'w') as f:
        json.dump(config, f)

def load_device_config():
    if not os.path.exists(STORAGE_FILE):
        return None
    
    try:
        with open(STORAGE_FILE, 'r') as f:
            config = json.load(f)
            return config.get("device_id")
    except:
        return None
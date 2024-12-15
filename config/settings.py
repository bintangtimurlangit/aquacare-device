# MQTT Settings
MQTT_BROKER = "broker.emqx.io"
MQTT_PORT = 1883
MQTT_KEEPALIVE = 60

# Metric Ranges
PH_RANGE = (6.0, 8.0)
TEMPERATURE_RANGE = (20.0, 30.0)
WATER_LEVEL_RANGE = (0, 100)

# Default Metric Values
DEFAULT_METRICS = {
    "ph_level": 7.0,
    "water_level": 100,
    "temperature": 25.0,
    "last_fed": None,
    "feeding_schedule": []
}

# Update Intervals (seconds)
METRIC_UPDATE_INTERVAL = 5
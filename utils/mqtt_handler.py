from paho.mqtt.client import Client as MQTTClient
import json
from config.settings import MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE

class MQTTHandler:
    def __init__(self, device_id, on_message_callback):
        self.device_id = device_id
        self.client = MQTTClient()
        self.client.client_id = device_id
        self.client.on_message = on_message_callback
        self.client.on_connect = self._on_connect
        
    def _on_connect(self, client, userdata, flags, rc, properties=None):
        """Callback when connected to MQTT broker"""
        print(f"Connected to MQTT broker with result code {rc}")
        self.client.subscribe(f"aquacare/{self.device_id}/feeding/schedule")
        self.client.subscribe(f"aquacare/{self.device_id}/control/#")
        
    def connect(self):
        self.client.connect(
            MQTT_BROKER, 
            MQTT_PORT, 
            keepalive=MQTT_KEEPALIVE
        )
        self.client.loop_start()
        
    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
        
    def publish(self, subtopic, payload):
        """Publish message to MQTT broker"""
        topic = f"aquacare/{self.device_id}/{subtopic}"
        self.client.publish(topic, json.dumps(payload))
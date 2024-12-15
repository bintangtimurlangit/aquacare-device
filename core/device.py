from datetime import datetime
import json
import time

from utils.mqtt_handler import MQTTHandler
from utils.qr_generator import generate_device_id, create_device_qr
from core.metrics import MetricsManager
from core.feeding import FeedingManager
from config.settings import METRIC_UPDATE_INTERVAL
from utils.storage import save_device_config, load_device_config

class AquaCareDevice:
    def __init__(self):
        # Try to load existing device ID first
        self.device_id = load_device_config()
        
        # If no existing device ID, generate new one
        if not self.device_id:
            self.device_id = generate_device_id()
            save_device_config(self.device_id)
            # Generate QR code only for new devices
            self.qr_path = create_device_qr(self.device_id)
            print(f"\nNew Device initialized with ID: {self.device_id}")
            print("\nScan this QR code to register your device:")
            print(self.qr_path)
        else:
            print(f"\nResuming with existing Device ID: {self.device_id}")
        
        # Initialize components
        self.metrics_manager = MetricsManager()
        self.feeding_manager = FeedingManager()
        self.mqtt = MQTTHandler(self.device_id, self.handle_message)
        
    def handle_message(self, client, userdata, msg):
        """Handle incoming MQTT messages"""
        topic = msg.topic
        try:
            payload = json.loads(msg.payload.decode())
            
            if "control" in topic:
                if payload.get("command") == "feed":
                    self.trigger_feeding('manual')
                elif "schedule" in payload:
                    # Update feeding schedules
                    self.feeding_manager.update_schedules(payload["schedule"])
                elif "test_mode" in payload:
                    # Set test mode based on the payload value
                    self.metrics_manager.test_mode = payload["test_mode"]
                    print(f"Test mode set to: {'ON' if payload['test_mode'] else 'OFF'}")
                    
                    # If turning test mode off, reset metrics to normal ranges
                    if not payload["test_mode"]:
                        self.metrics_manager.reset_metrics()
                    
        except Exception as e:
            print(f"Error handling message: {e}")
    
    def trigger_feeding(self, feed_type):
        """Execute feeding operation"""
        if self.feeding_manager.feed(feed_type):
            # Send confirmation back via MQTT only if feeding was successful
            self.mqtt.publish(f"aquacare/{self.device_id}/feeding/status", 
                            json.dumps({
                                "success": True,
                                "type": feed_type,
                                "timestamp": datetime.now().isoformat()
                            }))
    
    def publish_metrics(self):
        """Publish current metrics"""
        self.mqtt.publish("metrics", {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "metrics": self.metrics_manager.get_metrics()
        })
    
    def run(self):
        """Main device loop"""
        # Connect to MQTT broker
        print("Connecting to MQTT broker...")
        self.mqtt.connect()
        
        try:
            while True:
                # Simulate metric changes
                self.metrics_manager.simulate_changes()
                
                # Publish current metrics
                self.publish_metrics()
                
                # Check feeding schedule
                self.feeding_manager.check_schedule()
                
                time.sleep(METRIC_UPDATE_INTERVAL)
                
        except KeyboardInterrupt:
            print("Shutting down device...")
            self.mqtt.disconnect()
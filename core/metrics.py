import random
from config.settings import (
    DEFAULT_METRICS, 
    PH_RANGE, 
    TEMPERATURE_RANGE, 
    WATER_LEVEL_RANGE
)

class MetricsManager:
    def __init__(self):
        self.metrics = DEFAULT_METRICS.copy()
        self.test_mode = False
        self.test_scenario = 0
    
    def simulate_changes(self):
        """Simulate changes in aquarium metrics"""
        if self.test_mode:
            # Test different alert scenarios
            if self.test_scenario == 0:
                # Critical pH level
                self.metrics["ph_level"] = 5.8  # Below critical
            elif self.test_scenario == 1:
                # High temperature
                self.metrics["temperature"] = 30.5  # Above warning
            elif self.test_scenario == 2:
                # Critical water level
                self.metrics["water_level"] = 65  # Below critical
            
            self.test_scenario = (self.test_scenario + 1) % 3
        else:
            # Normal simulation
            self.metrics["ph_level"] += random.uniform(-0.1, 0.1)
            self.metrics["water_level"] -= random.uniform(0, 0.5)
            self.metrics["temperature"] += random.uniform(-0.2, 0.2)
            
            # Keep values within ranges
            self.metrics["ph_level"] = max(PH_RANGE[0], min(PH_RANGE[1], self.metrics["ph_level"]))
            self.metrics["water_level"] = max(WATER_LEVEL_RANGE[0], min(WATER_LEVEL_RANGE[1], self.metrics["water_level"]))
            self.metrics["temperature"] = max(TEMPERATURE_RANGE[0], min(TEMPERATURE_RANGE[1], self.metrics["temperature"]))
    
    def toggle_test_mode(self):
        """Toggle between normal and test mode"""
        self.test_mode = not self.test_mode
        print(f"Test mode: {'ON' if self.test_mode else 'OFF'}")
    
    def get_metrics(self):
        """Return current metrics"""
        return self.metrics
    
    def update_feeding_status(self, timestamp):
        """Update last feeding time"""
        self.metrics["last_fed"] = timestamp
    
    def reset_metrics(self):
        """Reset metrics to default values"""
        self.metrics = DEFAULT_METRICS.copy()
        self.test_scenario = 0
        print("Metrics reset to default values")
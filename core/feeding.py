from datetime import datetime
import json

class FeedingManager:
    def __init__(self):
        self.schedules = []
        self.last_feed_time = None
        
    def check_schedule(self):
        current_time = datetime.now()
        current_hour = current_time.strftime("%H:%M")
        current_day = str(current_time.isoweekday())  # 1-7 (Monday-Sunday)

        # Check if current time matches any schedule
        for schedule in self.schedules:
            if (schedule['time'] == current_hour and 
                current_day in schedule['days'].split(',')):
                print("\n🐟 Time to feed the fish! (Scheduled)")
                print(f"⏰ Schedule: {schedule['time']} on day {current_day}")
                return True
        return False

    def update_schedules(self, schedules):
        self.schedules = schedules
        print("\n📅 Feeding schedules updated:")
        for schedule in schedules:
            days = schedule['days'].split(',')
            days_text = ', '.join([self.get_day_name(int(d)) for d in days])
            print(f"⏰ {schedule['time']} on {days_text}")

    def feed(self, feed_type='manual'):
        current_time = datetime.now()
        
        # Prevent feeding too frequently (minimum 1 hour between feeds)
        if self.last_feed_time and (current_time - self.last_feed_time).seconds < 3600:
            print("\n⚠️ Warning: Too soon for another feeding!")
            print(f"Last feeding was at {self.last_feed_time.strftime('%H:%M')}")
            return False

        self.last_feed_time = current_time
        print(f"\n🐟 Feeding fish... ({feed_type})")
        print("✅ Feeding successful!")
        return True

    @staticmethod
    def get_day_name(day_number):
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return days[day_number - 1]
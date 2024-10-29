import time
from plyer import notification
import schedule

class DesktopNotifier:
    def __init__(self, title="Notification", message="This is a desktop notification", app_icon=None, timeout=5):
        """
        Initialize the DesktopNotifier with default values.
        
        :param title: The title of the notification.
        :param message: The message content of the notification.
        :param app_icon: The path to an icon file (.ico on Windows).
        :param timeout: The duration for which the notification is displayed (in seconds).
        """
        self.title = title
        self.message = message
        self.app_icon = app_icon
        self.timeout = timeout

    def send_notification(self):
        """
        Send a desktop notification with the given title, message, icon, and timeout.
        """
        notification.notify(
            title=self.title,
            message=self.message,
            app_icon=self.app_icon,
            timeout=self.timeout
        )

    def schedule_notification(self, delay_seconds=60):
        """
        Schedule a one-time notification after a specified delay in seconds.
        
        :param delay_seconds: Time to wait before showing the notification (in seconds).
        """
        print(f"Notification will be sent in {delay_seconds} seconds.")
        schedule_time = time.time() + delay_seconds
        schedule.every(delay_seconds).seconds.do(self.send_notification)

    def schedule_notification_at(self, time_str):
        """
        Schedule a notification at a specific time.
        
        :param time_str: Time string in "HH:MM" format for 24-hour time.
        """
        print(f"Notification will be sent at {time_str}.")
        schedule.every().day.at(time_str).do(self.send_notification)

    def run_scheduled_notifications(self):
        """
        Start the scheduler to run any scheduled notifications.
        """
        print("Scheduler is running...")
        while True:
            schedule.run_pending()
            time.sleep(1)

# Example usage:
if __name__ == "__main__":
    # Create a notifier instance
    notifier = DesktopNotifier(
        title="Break Reminder",
        message="It's time to take a break and stretch!",
        timeout=10
    )

    # Schedule a notification to appear after 10 seconds
    notifier.schedule_notification(delay_seconds=10)

    # Schedule a daily notification at a specific time (e.g., 14:00)
    notifier.schedule_notification_at("14:00")

    # Start the scheduler to keep the script running
    notifier.run_scheduled_notifications()

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
        print("Notification sent.")
        # Cancel the job to ensure it only runs once
        return schedule.CancelJob

    def schedule_notification(self, delay_seconds=60):
        """
        Schedule a one-time notification after a specified delay in seconds.
        
        :param delay_seconds: Time to wait before showing the notification (in seconds).
        """
        print(f"Notification will be sent in {delay_seconds} seconds.")
        schedule.every(delay_seconds).seconds.do(self.send_notification)

    def run_scheduled_notifications(self):
        """
        Run the scheduler and check for pending notifications once.
        """
        print("Scheduler is running for one notification...")
        while True:
            schedule.run_pending()
            time.sleep(1)
            # Stop the loop if no jobs remain in the scheduler
            if not schedule.get_jobs():
                print("No more scheduled jobs. Exiting.")
                break

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

    # Run the scheduler once for the notification
    notifier.run_scheduled_notifications()

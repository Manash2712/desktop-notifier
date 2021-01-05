import time
from plyer import notification


if __name__=='__main__':
    notification.notify(
        title = 'Please drink water now.',
        message = 'Water is good for health.',
        app_icon = '/home/manash/Desktop/DesktopNotifier/icon.ico',
        timeout = 10
    )
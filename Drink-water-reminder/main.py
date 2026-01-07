# Sends notification as a reminder to drink water

import time
from plyer import notification

while True:
    print("Please have a sip of water")
    notification.notify(title="Please drink somewater", message="It's time to have some water. Please have it.")
    time.sleep(60*60)
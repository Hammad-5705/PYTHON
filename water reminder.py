import time
from plyer import notification



notification.notify(
    title = f"Water Reminder".title(),
    message=" Time to drink waater" ,
    timeout=3
    )
# waiting time
time.sleep(7)

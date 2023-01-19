import os
import time
from win10toast import ToastNotifier

host = '8.8.8.8'
toaster = ToastNotifier()
notification_status = None

def internet_connection():
    request = os.system(f'ping -n 2 {host}')
    global notification_status

    if request == 0:
        if notification_status == True:
            toaster.show_toast('Internet ON', 'Internet is running NOW', threaded=True)
        print('Internet is ON')
        notification_status = False
    if request == 1:
        if notification_status == False:
            toaster.show_toast('Internet is OFF', 'Internet shuts DOWN', threaded=True)
        print('Internet Shuts DOWN')
        notification_status = True

# Run once for 'notification_status' change
internet_connection()
time.sleep(4)
os.system('cls')

while True:
    internet_connection()
    time.sleep(2)
    os.system('cls')

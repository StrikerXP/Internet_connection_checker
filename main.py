import os
import time
from win10toast import ToastNotifier

host = '8.8.8.8'
toaster = ToastNotifier()
notification_status = True
checker = 0

def internet_connection():
    request = os.system(f'ping -n 2 {host}')
    global notification_status
    global checker

    if request == 0:
        if checker == 1:
            notification_status = True
        checker = 0
        if notification_status == True:
            toaster.show_toast('Internet is ON', 'Internet is working', threaded=True)
            notification_status = False
        print('Internet is ON')
    if request == 1:
        if checker == 0:
            notification_status = True
        checker = 1
        if notification_status == True:
            toaster.show_toast('Internet is OFF', 'Internet shuts DOWN', threaded=True)
            notification_status = False
        print('Internet Shuts DOWN')

# Run once for 'notification_status' change
internet_connection()
time.sleep(2)
os.system('cls')

while True:
    internet_connection()
    time.sleep(2)
    os.system('cls')

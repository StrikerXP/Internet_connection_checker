import os
import time
import sys
from win10toast import ToastNotifier
from PySide2 import QtWidgets, QtGui

class SystemTray(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent):
        super().__init__(icon, parent)
        self.setToolTip('Internet Connection Checker')
        menu = QtWidgets.QMenu(parent)

        open_app = menu.addAction('Open terminal')
        open_app.triggered.connect(self.open_terminal)
        open_app.setIcon(QtGui.QIcon('icon.png'))

        _exit = menu.addAction('Exit')
        _exit.triggered.connect(lambda: sys.exit())

    def open_terminal(self):
        os.system('wmctrl -a :ACTIVE')


host = '8.8.8.8'
toaster = ToastNotifier()
notification_status = None
app = QtWidgets.QApplication(sys.argv)
qw = QtWidgets.QWidget()
tray = SystemTray(QtGui.QIcon('icon.png'), qw)
tray.show()
tray.showMessage('Internet Checker', 'Checks internet connection')
sys.exit(app.exec_())

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

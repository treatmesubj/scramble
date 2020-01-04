import win32con
import win32gui
import win32api
import win32process
import win32com.client
import subprocess
import time
import random


def get_hwnds_for_pid(pid):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                hwnds.append(hwnd)
            return True
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds


# window = subprocess.Popen(
#    "disco.bat", creationflags=subprocess.CREATE_NEW_CONSOLE)

username = win32api.GetUserName()
s = win32com.client.Dispatch('SAPI.SpVoice')
voices = [i for i in s.GetVoices()]
s.Voice = voices[1]
s.Rate = 3
win32api.Beep(1050, 1000)
s.Speak(f"Congratulations, {username}. Enjoy.")

for hwnd in get_hwnds_for_pid(window.pid):
    print(hwnd, "=>", win32gui.GetWindowText(hwnd))
    for i in range(1, 100):
        win32gui.MoveWindow(hwnd, random.randint(1, 1000),
                            random.randint(1, 500), 700, 400, 1)
        time.sleep(0.1)


win32gui.SendMessage(hwnd, win32con.WM_CLOSE, 0, 0)

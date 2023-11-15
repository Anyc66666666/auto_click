import pyautogui
import time

while True:
    x, y = pyautogui.position()
    # 返回鼠标的坐标
    print(f'当前鼠标坐标 : ({x}, {y})')
    time.sleep(1)

# Pyinstaller -F -i coordinate.ico coordinate.py

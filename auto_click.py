import re
import sys
import time

import pyautogui
import os

print("请在配置文件 config.txt 中输入所有的坐标，以回车键分隔\n例如:\n(1,1)\n(2,2)\n(3,3)")

coordinates = []
pattern = r"\((-?\d+),(-?\d+)\)"
contents = ""
try:
    with open('config.txt', encoding='utf-8') as config:
        print("-------------------------")
        print("------正在读取配置文件------")
        contents = config.read()
        contents = contents.rstrip()
except Exception:
    print("配置文件 config.txt 未找到")
    time.sleep(5)
    sys.exit()

if contents == "":
    print("配置文件错误")
    sys.exit()

content_list = contents.split("\n")
for content in content_list:
    match = re.match(pattern, content)

    if match:
        # 提取 x 和 y 值
        x = int(match.group(1))
        y = int(match.group(2))
        coordinates.append({
            "x": x,
            "y": y
        })

if len(coordinates) == 0:
    print("坐标数据错误，未匹配到坐标")
    sys.exit()

while True:
    for co in coordinates:
        pyautogui.click(co.x, co.y)
        time.sleep(1)

# Pyinstaller -F -i auto_click.ico auto_click.py

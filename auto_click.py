import re
import sys
import time
import logging
import os

import pyautogui

print("请在配置文件 config.txt 中输入所有的坐标，以回车键分隔\n例如:\n(1,1)\n(2,2)\n(3,3)\n\n")

coordinates = []
pattern = r"\((-?\d+),(-?\d+)\)"
contents = ""
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(fmt='%(asctime)s[%(levelname)s]:%(message)s')

sh = logging.StreamHandler()
logger.addHandler(sh)
sh.setFormatter(formatter)
sh.setLevel(logging.INFO)
try:
    with open('config.txt', encoding='utf-8') as config:
        print("----------------------------")
        print("------正在读取配置文件------")
        contents = config.read()
        contents = contents.rstrip()
except Exception:
    logger.error("配置文件 config.txt 未找到")
    time.sleep(5)
    sys.exit()

if contents == "":
    logger.error("配置文件错误")
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
    logger.error("坐标数据错误，未匹配到坐标")
    sys.exit()
print("------读取配置文件成功------\n------检测到的坐标如下------")
for co in coordinates:
    print(f"({co['x']},{co['y']})")

while True:
    time.sleep(3)
    for co in coordinates:
        logger.info(f"点击一次 ({co['x']},{co['y']})")
        pyautogui.click(co["x"], co["y"])
        time.sleep(2)

# Pyinstaller -F -i auto_click.ico auto_click.py

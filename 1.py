import pyautogui
import pyperclip
import time
import random
from datetime import datetime, timedelta

def get_msg():
    """所有可能发送的消息，每条消息空格分开"""
    contents = [
        "想你了",
        "亲亲美厶",
        "想美厶了",
        "老婆大王我想你了",
        "大王我想你了",
    ]
    return contents

def send(msg):
    """发送消息的功能"""
    # 复制需要发送的内容到粘贴板
    pyperclip.copy(msg)
    # 模拟键盘 ctrl + v 粘贴内容
    pyautogui.hotkey('ctrl', 'v')
    # 发送消息
    pyautogui.press('enter')
    # 退出窗口
    pyautogui.hotkey('ctrl', 'alt', 'w')

def send_msg(friend):
    """发送消息给指定好友"""
    # Ctrl + alt + w 打开微信
    pyautogui.hotkey('ctrl', 'alt', 'w')
    # 搜索好友
    pyautogui.hotkey('ctrl', 'f')
    # 复制好友昵称到粘贴板
    pyperclip.copy(friend)
    # 模拟键盘 ctrl + v 粘贴
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    # 回车进入好友消息界面
    pyautogui.press('enter')

    # 从消息列表中随机挑选一条消息并发送
    msg = random.choice(get_msg())
    send(msg)

def generate_random_times(start_time, end_time, num_times):
    """生成从start_time到end_time之间的num_times个随机时间点"""
    time_points = []
    total_seconds = int((end_time - start_time).total_seconds())
    for _ in range(num_times):
        random_seconds = random.randint(0, total_seconds)
        time_points.append(start_time + timedelta(seconds=random_seconds))
    return sorted(time_points)

def check_and_send_messages(friend, time_points):
    """在指定的时间点发送消息"""
    for target_time in time_points:
        while True:
            current_time = datetime.now()
            if current_time >= target_time:
                send_msg(friend)
                break
            # 每5钟检查一次
            time.sleep(300)

if __name__ == '__main__':
    friend_name = "厶"  # 这里填写你微信好友的名字
    current_time = datetime.now()
    end_of_day = datetime.combine(current_time.date(), datetime.max.time())
    time_points = generate_random_times(current_time, end_of_day, 10)  # 生成10个随机时间点
    check_and_send_messages(friend_name, time_points)

import pyautogui
import keyboard
import time

y_ = 585
time.sleep(3)
keyboard.press('shift')
for i in range(3):
    x_ = 815
    for j in range(9):
        pyautogui.click(x=x_, y=y_, button='left', clicks=2)
        x_ += 35
    y_ += 35
keyboard.release('shift')
pyautogui.click(x=960, y=525, button='left')

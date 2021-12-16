from pyautogui import click
from time import time, sleep

sleep(5)
now = time()

while time() - now <= 100:
    click(button="right")


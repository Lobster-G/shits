from pyautogui import moveTo, click
from time import sleep, time

# 1040б 945
now = time()
sleep(2)
while time() - now <= 100:
    print(time() - now)
    moveTo(1040, 945)
    # sleep(0.1)
    click(button="left")
    # sleep(0.1)
    moveTo(955, 630)
    # sleep(0.1)
    click(button="left")
    # sleep(0.1)

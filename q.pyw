from pyautogui import pixel, mouseDown, mouseUp, press, moveTo, click
from time import sleep


def is_pecked():
    float_col = pixel(1758, 294)
    if float_col[0] not in float_col_range[0]\
            and float_col[1] not in float_col_range[1]\
            and float_col[2] not in float_col_range[2]:
        return True


def catch():
    def move_n_click(x: int, y: int, button: str, delay=(0.2, 0.2)):
        sleep(delay[0])
        moveTo(x, y)
        sleep(delay[1])
        click(button=button)

    mouseDown(button="right")
    sleep(0.2)
    mouseDown(button="left")
    sleep(1)
    mouseUp(button="right")
    while pixel(1633, 797) == (29, 54, 194):                # вытащил или нет
        sleep(1)                                            # нет
        continue
    else:                                                   # да
        mouseUp(button="left")
        sleep(3)
        press("space")
        sleep(3)
    cage_status = pixel(103, 195)
    if cage_status[0] not in cage_col_range[0]\
            and cage_status[1] not in cage_col_range[1]\
            and cage_status[2] not in cage_col_range[2]:                  # полный садок
        press("t")
        sleep(0.2)
        moveTo(960, 920)
        sleep(0.2)
        click(button="left")
        # move_n_click(960, 920, "left")
        sleep(2)
        moveTo(780, 680)
        sleep(0.2)
        click(button="left")
        # move_n_click(780, 680, "left", (2, 0.2))
        sleep(2)
        moveTo(870, 850)
        sleep(0.2)
        click(button="left")
        # move_n_click(870, 850, "left", (2, 0.2))
    else:                                                   # заброс
        mouseDown(button="left")
        sleep(0.2)
        mouseUp(button="left")
        sleep(3)


float_col_range = [range(180, 195), range(180, 195), range(180, 195)]           # цвета попловка
cage_col_range = [range(225, 255), range(225, 255), range(225, 255)]            # цвета садка

sleep(2 )
while True:
    try:
        if is_pecked():
            catch()
    except:
        if is_pecked():
            catch()
    sleep(1)

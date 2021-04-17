from tkinter import *
import pyautogui
import keyboard
import time
import random


def movement(direction):
    keyboard.press(direction)
    a = random.uniform(1.13, 1.16)
    time.sleep(a)
    keyboard.release(direction)
    time.sleep(a)


def mine():
    time.sleep(3)
    pyautogui.mouseDown(button='left')
    while True:
        # movement('a')
        # movement('d')
        if keyboard.is_pressed('esc'):
            pyautogui.mouseUp('left')
            break


def attack():
    time.sleep(3)
    while True:
        pyautogui.click(button='left')
        if keyboard.is_pressed('esc'):
            break
        time.sleep(0.7)


def fish():
    time.sleep(3)
    pyautogui.mouseDown(button='right')
    while True:
        if keyboard.is_pressed('esc'):
            pyautogui.mouseUp('right')
            break
        time.sleep(0.7)


main_window = Tk()
main_window.title('Choose your champion')
main_window.protocol('WM_DELETE_WINDOW', main_window.quit())
main_window.geometry('{}x{}'.format(400, 100))
main_window.attributes('-topmost', True)
mine_button = Button(text='Mine', command=mine, width=10, height=10, font='Arial 16')
mine_button.pack(side='left')
attack_button = Button(text='Attack', command=attack, width=11, height=10, font='Arial 16')
attack_button.pack(side='left')
fish_button = Button(text='Fishing', command=fish, width=10, height=10, font='Arial 16')
fish_button.pack(side='right')
main_window.mainloop()

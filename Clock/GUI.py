from tkinter import Tk, Label, BOTTOM, TOP, Entry, Button
from time import time, localtime, strftime
from ctypes import windll


global_screen_width = windll.user32.GetSystemMetrics(78)
global_screen_height = windll.user32.GetSystemMetrics(79)
screen_top = windll.user32.GetSystemMetrics(77)


class CityEnter:
    def __init__(self, master):
        self.main_window = master
        self.main_window.title("Enter city")
        self.main_window.geometry(f"{190}x{100}")
        self.main_window.wm_attributes("-topmost", True)
        self.manual = Label(text="Введите ваш город в формате "
                                 "\n 'Название','Страна(сокращение)'", )
        self.manual.pack()
        self.city_input = Entry()
        self.city_input.insert(0, "Moscow,RU")
        self.city_input.place(x=34, y=40)
        self.submit = Button(text="Ввести", width=10)
        self.submit.pack(side=BOTTOM)


class Clocks:
    def __init__(self, master):
        self.width, self.height = 76, 115
        self.main_window = master
        self.main_window.resizable(False, False)
        self.main_window.overrideredirect(True)
        self.main_window.wm_attributes("-topmost", True)
        self.main_window.wm_attributes("-transparentcolor", "black")
        self.main_window.geometry(f'{self.width}x{self.height}+'
                                  f'{global_screen_width - self.width}+{screen_top}')
        self.time_output = Label(width=self.width,
                                 bg='black', fg='white',
                                 font='TimesNewRoman 12')
        self.weather_output = Label(width=self.width,
                                    bg='black', fg='white',
                                    font='TimesNewRoman 12',
                                    anchor='s')
        self.time_output.pack(side=TOP)
        self.weather_output.pack(side=BOTTOM)

    def tick(self):
        self.time_output.after(1000, Clocks.tick)
        self.time_output.config(text=strftime("%X\n%a %d", localtime(time())))

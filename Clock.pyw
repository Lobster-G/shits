from ctypes import windll
import requests
from time import time, localtime, strftime
from tkinter import *

city_id = 551847
app_id = "169b613e6ee116a4e0b22d48ffee53f6"


global_screen_width = windll.user32.GetSystemMetrics(78)
global_screen_height = windll.user32.GetSystemMetrics(79)
screen_top = windll.user32.GetSystemMetrics(77)


def tick():
    time_output.after(1000, tick)
    time_output.config(text=strftime("%X\n%a %d", localtime(time())))


def weather():
    weather_output.after(3600000, weather)
    res = requests.get(
        "http://api.openweathermap.org/data/2.5/weather",
        params={'id': city_id, 'units': 'metric', 'lang': 'en', 'APPID': app_id})
    data = res.json()
    if data['main']['temp'] > 0:
        cur_temp = '+' + str(round(data['main']['temp'])) + ' °C'
    else:
        cur_temp = str(round(data['main']['temp'])) + ' °C'
    cur_weather = '\n' + data['weather'][0]['description'].capitalize() +\
                  '\n' + cur_temp +\
                  '\n' + str(data['wind']['speed']) + ' m/s'
    weather_output.config(text=cur_weather)


window = Tk()
window.overrideredirect(True)
width, height = 76, 100
window.geometry(f'{width}x{height}+{global_screen_width - width}+{screen_top}')
time_output = Label(width=width,
                    bg='black', fg='white',
                    font='TimesNewRoman 12')
weather_output = Label(width=width,
                       bg='black', fg='white',
                       font='TimesNewRoman 12',
                       anchor='s')
window.wm_attributes("-topmost", True)  # поверх всех окон
window.wm_attributes("-transparentcolor", "black")  # прозрачность
time_output.pack(side=TOP)
weather_output.pack(side=BOTTOM)
time_output.after_idle(tick)
weather_output.after_idle(weather)
window.mainloop()

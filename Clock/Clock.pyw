from ctypes import windll
from requests import get
from time import time, localtime, strftime
from tkinter import Tk, Label, BOTTOM, TOP, Entry, Button

global_screen_width = windll.user32.GetSystemMetrics(78)
global_screen_height = windll.user32.GetSystemMetrics(79)
screen_top = windll.user32.GetSystemMetrics(77)

app_id = "169b613e6ee116a4e0b22d48ffee53f6"


def pre_main():
    global city
    city = "Moscow,RU"
    city = get_city.get()
    enter_city.destroy()
    res = get("http://api.openweathermap.org/data/2.5/find",
              params={'q': city, 'type': 'like', 'units': 'metric', 'APPID': app_id})
    data = res.json()
    global city_id
    # noinspection PyRedeclaration
    city_id = data['list'][0]['id']
    with open("./data.txt", "a") as file:
        file.write(str(city_id))
    main()


def main():
    width, height = 76, 115

    def tick():
        time_output.after(1000, tick)
        time_output.config(text=strftime("%X\n%a %d", localtime(time())))

    def weather():
        nonlocal height
        weather_output.after(3600000, weather)
        res = get(
            "http://api.openweathermap.org/data/2.5/weather",
            params={'id': city_id, 'units': 'metric', 'lang': 'en', 'APPID': app_id})
        data = res.json()
        if len(data['weather'][0]['description'].capitalize()) > len("Clear sky"):
            description = data['weather'][0]['description'].capitalize().split()[0] + \
                          "\n" + data['weather'][0]['description'].capitalize().split()[1]
        else:
            description = data['weather'][0]['description'].capitalize()
            height = 115
        if data['main']['temp'] > 0:
            cur_temp = '+' + str(round(data['main']['temp'])) + ' °C'
        else:
            cur_temp = str(round(data['main']['temp'])) + ' °C'
        cur_speed = str(data['wind']['speed']) + ' m/s'

        cur_weather = description + '\n' + cur_temp + '\n' + cur_speed
        weather_output.config(text=cur_weather)

    window = Tk()
    window.resizable(False, False)
    window.overrideredirect(True)

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


try:
    with open("C:/Projects/Python/Clock/data.txt", "r") as f:
        global city_id
        city_id = int(f.readline().strip())

        main()
except FileNotFoundError:
    with open("C:/Projects/Python/Clock/data.txt", "w") as f:
        f.write("Exist")
        enter_city = Tk()
        enter_city.title('')
        enter_city.geometry(f'{190}x{100}')
        enter_city.wm_attributes("-topmost", True)  # поверх всех окон
        enter_manual = Label(text="Введите ваш город в формате \n 'Название','Страна(сокращение)'", )
        enter_manual.pack()
        get_city = Entry()
        get_city.insert(0, "Moscow,RU")
        get_city.place(x=34, y=40)
        submit = Button(text="Ввести", command=pre_main, width=10)
        submit.pack(side=BOTTOM)
        enter_city.mainloop()

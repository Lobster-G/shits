from tkinter import Tk
from time import strftime, localtime, time
from modules.GUI import CityEnter, Clocks
from modules.weather import *
from modules.data import create_df, abspath
from modules.fixed_clipboard import fixing
from threading import Thread


def pack_weather_info(component):
    component.after(3600000, pack_weather_info)
    component.config(text=get_weather_info(city_id))


def main():
    def tick():
        root.time_output.after(1000, tick)
        root.time_output.config(text=strftime("%X\n%a %d", localtime(time())))

    parent = Tk()
    root = Clocks(parent)
    root.time_output.after_idle(tick)
    root.weather_output.after_idle(pack_weather_info, root.weather_output)
    parent.mainloop()


def get_and_destroy():
    global city_id
    try:
        city_id = get_city_id(msg.city_input.get())
    except IncorrectAPIKey as e:
        if len(e.args[1]) > 12:
            error = "".join([f"{i}\n" for i in e.__str__().rsplit(maxsplit=1)])
        else:
            error = e.__str__()
        msg.city_input.delete(0, len(msg.city_input.get()))
        return msg.manual.config(text=f"{error}")
    temp.destroy()
    create_df("data", city_id)


try:
    with open(f"{abspath('data.txt')}", "r") as f:
        city_id = int(f.readline().strip().split()[1])
    t1 = Thread(target=main)
    t2 = Thread(target=fixing)
    t1.start()
    t2.start()
except FileNotFoundError:
    temp = Tk()
    msg = CityEnter(temp)
    msg.submit.config(command=get_and_destroy)
    temp.mainloop()
    main()

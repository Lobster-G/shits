from tkinter import Tk
from time import strftime, localtime, time
from Python.Clock.modules.GUI import *
from Python.Clock.modules.weather import *
from Python.Clock.modules.data import create_df


def main():
    def tick():
        root.time_output.after(1000, tick)
        root.time_output.config(text=strftime("%X\n%a %d", localtime(time())))

    parent = Tk()
    root = Clocks(parent)
    root.time_output.after_idle(tick)
    root.weather_output.after_idle(get_weather_info, city_id, root.weather_output)
    parent.mainloop()


def destroy():
    global city_id
    city_id = get_city_id(msg.city_input.get())
    temp.destroy()
    create_df("data", city_id)


try:
    with open("data.txt", "r") as f:
        print()
        city_id = int(f.readline().strip().split()[1])
    main()
except FileNotFoundError:
    temp = Tk()
    msg = CityEnter(temp)
    msg.submit.config(command=destroy)
    temp.mainloop()
    main()

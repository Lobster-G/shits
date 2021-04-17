from tkinter import *
from winsound import PlaySound, SND_ALIAS, SND_ASYNC


root = Tk()
root.overrideredirect(True)
width, height = 300, 120
root.attributes('-topmost', True)
root.geometry('{}x{}+{}+{}'.format(width, height, 2310, 380))        # 810, 380
message = Label(text='Встань, отдохни',
                width=width, height=height,
                bg='#393d3f', fg='white',
                font='TimesNewRoman 20').pack()
PlaySound('C:/Projects/Python/StandUp/prowu.wav', SND_ALIAS | SND_ASYNC)
root.after(10000, lambda: root.destroy())
root.mainloop()
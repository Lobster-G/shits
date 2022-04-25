from tkinter import *

root = Tk()
root.overrideredirect(True)
width, height = 300, 120
root.attributes('-topmost', True)
root.geometry(f'{width}x{height}+{2310}+{380}')  # 810, 380
message = Label(text='Встань, отдохни',
                width=width, height=height,
                bg='#393d3f', fg='white',
                font='TimesNewRoman 20')
message.pack()
root.after(10000, lambda: root.destroy())
root.mainloop()

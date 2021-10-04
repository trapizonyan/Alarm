from tkinter import *
import datetime
import time
from Alarm import Alarm
from Clock import Clock


class Interface:
    def __init__(self):
        self.ob_al = Alarm()
        self.ob_clock = Clock()
        self.root = Tk()
        self.root['bg'] = '#242424'
        self.root.title('Будильник')
        self.root.geometry('400x600')

        self.root.resizable(width=False, height=False)

        self.clock_label = Label(
            self.root, text="", font=('Calibri', 18), fg='white', bg="#383838")
        self.clock_label.place(width=400)
        self.func_clock()
        title_day = Label(self.root, text='День', padx=100,
                          fg='white', bg='#242424', font=('Calibri', 14))
        title_day.place(x=30, y=60, width=50, height=20)
        self.volume_day = Entry(self.root, font=('Calibri', 18))
        self.volume_day.place(x=30, y=90, width=50, height=25)

        title_h = Label(self.root, text='Часы', padx=100,
                        fg='white', bg='#242424', font=('Calibri', 14))
        title_h.place(x=175, y=60, width=50, height=20)
        self.volume_h = Entry(self.root, font=('Calibri', 18))
        self.volume_h.place(x=175, y=90, width=50, height=25)

        title_m = Label(self.root, text='Мин',
                        fg='white', bg='#242424', font=('Calibri', 14))
        title_m.place(x=310, y=60, width=50, height=20)
        self.volume_m = Entry(self.root, font=('Calibri', 18))
        self.volume_m.place(x=310, y=90, width=50, height=25)

        title_s = Label(self.root, text='Рингтон',
                        fg='white', bg='#242424', font=('Calibri', 14))
        title_s.place(x=150, y=160, width=100, height=20)

        self.sounds = Listbox(width=25, font=('Calibri', 12))
        for x, y in enumerate(self.ob_al.music_list):
            self.sounds.insert(x+1, y)
        self.sounds.place(x=98, y=190)

        bt = Button(self.root, text='Установить будильник', font=('Calibri', 12),
                    command=self.button_set_alarm)
        bt.place(x=100, y=410, width=200, height=50)

        bt = Button(self.root, text='Остановить будильник', font=('Calibri', 12),
                    command=self.ob_al.music_stop)
        bt.place(x=100, y=470, width=200, height=50)

        self.root.mainloop()

    def volues(self):
        self.day = self.volume_day.get()
        self.hour = self.volume_h.get()
        self.minute = self.volume_m.get()
        self.track = self.sounds.get(ANCHOR)

    def button_set_alarm(self):
        self.volues()
        if self.day != '' and self.hour != '' and self.minute != '' and self.track != '':
            self.ob_al.set_alarm(self.day, self.hour, self.minute, self.track)

        else:
            self.ob_al.music_load(self.track)

    def func_clock(self):

        self.clock_label.config(text=self.ob_clock.format_clock())
        self.clock_label.after(1000, self.func_clock)

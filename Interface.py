from tkinter import *
import datetime
from Alarm import Alarm


class Interface:
    def __init__(self):
        self.obj = Alarm()

        root = Tk()
        root['bg'] = 'black'
        root.title('Будильник')
        root.geometry('400x600')

        root.resizable(width=False, height=False)

        title = Label(root, text='Будильник', padx=10,
                      fg='white', bg='black', font=('Calibri', 16))
        title.pack()
        title_day = Label(root, text='День', padx=100,
                          fg='white', bg='black', font=('Calibri', 14))
        title_day.place(x=30, y=60, width=50, height=20)
        self.volume_day = Entry(root, font=('Calibri', 18))
        self.volume_day.place(x=30, y=90, width=50, height=25)

        title_h = Label(root, text='Часы', padx=100,
                        fg='white', bg='black', font=('Calibri', 14))
        title_h.place(x=175, y=60, width=50, height=20)
        self.volume_h = Entry(root, font=('Calibri', 18))
        self.volume_h.place(x=175, y=90, width=50, height=25)

        title_m = Label(root, text='Мин',
                        fg='white', bg='black', font=('Calibri', 14))
        title_m.place(x=310, y=60, width=50, height=20)
        self.volume_m = Entry(root, font=('Calibri', 18))
        self.volume_m.place(x=310, y=90, width=50, height=25)

        title_s = Label(root, text='Рингтон',
                        fg='white', bg='black', font=('Calibri', 14))
        title_s.place(x=150, y=160, width=100, height=20)

        self.sounds = Listbox(width=25, font=('Calibri', 12))
        for x, y in enumerate(self.obj.music_list):
            self.sounds.insert(x+1, y)
        self.sounds.place(x=98, y=190)

        bt = Button(root, text='Установить будильник', font=('Calibri', 12),
                    command=self.volumes)
        bt.place(x=100, y=410, width=200, height=50)

        bt = Button(root, text='Остановить будильник', font=('Calibri', 12),
                    command=self.obj.music_stop)
        bt.place(x=100, y=470, width=200, height=50)

        root.mainloop()

    def volumes(self):
        self.day = self.volume_day.get()
        self.hour = self.volume_h.get()
        self.minute = self.volume_m.get()
        self.track = self.sounds.get(ANCHOR)
        if self.day != '' and self.hour != '' and self.minute != '' and self.track != '':
            self.obj.start_app(self.day, self.hour, self.minute, self.track)
        else:
            self.obj.music_load(self.track)

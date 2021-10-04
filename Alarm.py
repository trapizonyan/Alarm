import datetime
from pygame import mixer
from time import sleep, time
mixer.init()


class Alarm:

    def __init__(self):
        self.music_list = {'one': 'media/1.mp3', 'two': 'media/2.mp3',
                           'three': 'media/3.mp3', 'four': 'media/4.mp3'}

    def start_app(self, d, h, m, x):

        while True:
            time_now = datetime.datetime.now()

            if str(time_now.day) == d and str(time_now.hour) == h and str(time_now.minute) == m:
                self.music_load(x)
                break
            sleep(2)

    def music_load(self, x):

        mixer.music.load(self.music_list[x])
        mixer.music.play()
        return mixer.music.get_busy()

    def music_stop(self):
        mixer.music.stop()
        return mixer.music.get_busy()

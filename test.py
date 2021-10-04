import unittest
from Alarm import Alarm
from Interface import Interface
from Clock import Clock


class TestAlarm(unittest.TestCase):

    def setUp(self):
        self.ob_alarm = Alarm()
        self.ob_cl = Clock()

    def test_music_load(self):
        self.assertEqual(self.ob_alarm.music_load('one'), True)

    def test_music_stop(self):
        self.assertEqual(self.ob_alarm.music_stop(), False)

    def test_music_list(self):
        self.assertEqual(self.ob_alarm.music_list['two'], 'media/2.mp3')

    def test_format_clock(self):
        self.assertEqual(self.ob_cl.format_clock(), '02:34:57')


if __name__ == '__main__':
    unittest.main()

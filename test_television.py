import pytest
from television import *


class Test:
    def setup_method(self):
        self.tele1 = Television()

    def teardown_method(self):
        del self.tele1

    def test_init(self):
        # Test if television has correct default values
        assert self.tele1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        # Test if power turns on
        self.tele1.power()
        assert self.tele1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        # Test if power turns off
        self.tele1.power()
        assert self.tele1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        # Test to ensure channel_up isn't operational with power off
        self.tele1.channel_up()
        assert self.tele1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        # Test to ensure channel_down isn't operational with power off
        self.tele1.channel_up()
        self.tele1.channel_up()
        self.tele1.channel_down()
        assert self.tele1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        # Test to ensure volume_up isn't operational with power off
        self.tele1.volume_up()
        assert self.tele1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        # Test to ensure volume_down isn't operational with power off
        self.tele1.volume_up()
        self.tele1.volume_up()
        self.tele1.volume_down()
        assert self.tele1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        # Test if volume is muted
        self.tele1.power()
        self.tele1.volume_up()
        self.tele1.mute()
        assert self.tele1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        # Test if volume returns when unmuted
        self.tele1.mute()
        assert self.tele1.__str__() == 'Power = True, Channel = 0, Volume = 1'

    def test_channel_up(self):
        # Test if channel increases
        self.tele1.power()
        self.tele1.channel_up()
        assert self.tele1.__str__() == 'Power = True, Channel = 1, Volume = 0'

        # Test if channel loops after reaching 3
        self.tele1.channel_up()
        self.tele1.channel_up()
        self.tele1.channel_up()
        assert self.tele1.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        # Test if channel decreases
        self.tele1.power()
        self.tele1.channel_up()
        self.tele1.channel_down()
        assert self.tele1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        # Test if channel loops after reaching 0
        self.tele1.channel_down()
        assert self.tele1.__str__() == 'Power = True, Channel = 3, Volume = 0'

    def test_volume_up(self):
        # Test if volume increases
        self.tele1.power()
        self.tele1.volume_up()
        assert self.tele1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        # Test if volume maxes out at 2
        self.tele1.volume_up()
        self.tele1.volume_up()
        assert self.tele1.__str__() == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        # Test if volume decreases
        self.tele1.power()
        self.tele1.volume_up()
        self.tele1.volume_down()
        assert self.tele1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        # Test if volume cannot go lower than 0
        self.tele1.volume_down()
        assert self.tele1.__str__() == 'Power = True, Channel = 0, Volume = 0'
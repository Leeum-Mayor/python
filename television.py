class Television:
    """
    A class representing actions for a television object
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Sets default values of television object
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggles power on and off
        """
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        Toggles muted state on and off
        """
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self) -> None:
        """
        Changes channel up
        """
        if self.__status == True:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Changes channel down
        """
        if self.__status == True:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Turns volume up
        """
        if self.__status == True:
            self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Turns volume down
        """
        if self.__status == True:
            self.mute()

            if self.__volume >= 1:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to see power, channel, and volume
        :return: Status of power, channel, and volume
        """
        if self.__muted == True:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'


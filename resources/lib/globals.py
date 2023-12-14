from enum import Enum

class Actions(Enum):
    Navigate = "navigate"
    Play = "play"
    Search = "search"

    def __str__(self):
        return self._value_
    
    def __eq__(self, __value):
        return self.__str__() == __value
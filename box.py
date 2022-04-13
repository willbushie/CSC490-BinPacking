# imports

from operator import length_hint

from matplotlib import widgets


class box:
    def __init__(self,height,length,width) -> None:
        self.placed = False
        self.height = height
        self.length = length
        self.width = width
        self.volume = self.height * self.length * self.width
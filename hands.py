from dices import *

class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        super().__init__()

        for _ in range(size):
            self.append(die_class())
        self.sort()

    @property
    def total(self):
        return sum(self)

    def roll(self, size=0, *args, **kwwargs):
        self.__init__(size=size, die_class=D20)
        for _ in self:
            return self.total

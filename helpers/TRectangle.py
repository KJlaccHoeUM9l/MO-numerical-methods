import math
from helpers.TPoint import point


class rectangle:
    width = 0.0
    height = 0.0
    leftUp = point(0.0, 0.0)
    rightDown = point(0.0, 0.0)
    center = point(0.0, 0.0)

    def __init__(self, leftUp, rightDown):
        self.leftUp = leftUp
        self.rightDown = rightDown
        self.width = self.rightDown.x - self.leftUp.x
        self.height = self.leftUp.y - self.rightDown.y
        self.center = point((self.leftUp.x + self.rightDown.x) / 2.0,
                            (self.leftUp.y + self.rightDown.y) / 2.0)


    def getDiam(self):
        return math.sqrt(self.width**2 + self.height**2)

    def __str__(self) -> str:
        return 'Rectangle'

import matplotlib.pyplot as plt
from abc import ABC, ABCMeta
from helpers.TPoint import point
import matplotlib.patches as patches


class IAnimated(ABC):
    __metaclass__ = ABCMeta

    rectangles = []

    def __init__(self):
        self.rectangles.clear()

    def animation2D(self):
        fig, axes = plt.subplots()
        plt.xlim(-2,2)
        plt.ylim(-1,1)
        plt.ion()

        iteration = 0
        for rect in self.rectangles:
            leftUp = rect.leftUp
            rightDown = rect.rightDown
            leftDown = point(leftUp.x, rightDown.y)
            width = rect.width
            height = rect.height

            axes.add_patch(
                patches.Rectangle((leftDown.x, leftDown.y), width, height, color='g', linewidth=1, fill=0))

            plt.draw()
            plt.pause(0.01)

            iteration += 1
            if iteration == 100:
                break

        input('Press any kay to continue:')
        plt.ioff()

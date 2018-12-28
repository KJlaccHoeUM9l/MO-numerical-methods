import matplotlib.pylab as plt
import numpy as np
from py_expression_eval import Parser
from abc import ABC, ABCMeta, abstractmethod
from sympy.plotting import plot3d
from sympy import *
import matplotlib.patches as patches

from helpers.TPoint import point

class optimizable(ABC):
    __metaclass__ = ABCMeta

    targetExpression = 'x^2+y^2'
    a = -2
    b = 2
    c = -1
    d = 1

    def __init__(self, targetFunction, a, b, c, d):
        self.targetExpression = targetFunction
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        self.density = 50
        self.expression = Parser().parse(self.targetExpression)
        self.rectangles = []  # For animation

    def printExpression(self):
        print('Q(x,y) = ' + self.targetExpression)

    def Q(self, x, y):
        return self.expression.evaluate({'x': x, 'y': y})

    def initPlot(self, plotName, X, Y):
        x, y = np.meshgrid(X, Y)
        z = self.getFunctionValues(X, Y)

        # Create plot
        plt.figure(plotName)
        contours = plt.contour(x, y, z, 15)  # Линии уровня целевой функции (последний аргумент - количество линий)
        plt.clabel(contours, inline=True, fontsize=8)  # Значение уровня на линиях (последний аргумент - размер шрифта)

        return plt

    def showFunction3D(self):
        x, y = symbols('x y')
        plot3d(self.targetExpression, (x, self.a, self.b), (y, self.c, self.d))

    def showFunction2D(self):
        X = np.linspace(self.a, self.b, self.density)
        Y = np.linspace(self.c, self.d, self.density)

        self.initPlot(self.targetExpression, X, Y).show(self.targetExpression)

    def showMin2D(self):
        X = np.linspace(self.a, self.b, self.density)
        Y = np.linspace(self.c, self.d, self.density)

        newPlot = self.initPlot('Min value', X, Y)
        newPlot.plot(self.x_.x, self.x_.y, self.Q_, 'rs', label='optimum')
        newPlot.show()

    def animation2D(self):
        tmp, axes = plt.subplots()
        plt.xlim(self.a, self.b)
        plt.ylim(self.c, self.d)

        X = np.linspace(self.a, self.b, self.density)
        Y = np.linspace(self.c, self.d, self.density)
        x, y = np.meshgrid(X, Y)
        z = self.getFunctionValues(X, Y)
        axes.contourf(x, y, z, 15)

        plt.ion()
        iteration = 0
        for rect in self.rectangles:
            leftUp = rect.leftUp
            rightDown = rect.rightDown
            leftDown = point(leftUp.x, rightDown.y)
            width = rect.width
            height = rect.height

            axes.add_patch(
                patches.Rectangle((leftDown.x, leftDown.y), width, height, color='r', linewidth=1, fill=0))

            plt.draw()
            plt.pause(0.01)

            iteration += 1
            if iteration == 200:
                break
        plt.ioff()

    def getFunctionValues(self, X, Y):
        z = []
        for i in X:
            tmp = []
            for j in Y:
                tmp.append(self.Q(i, j))
            z.append(tmp)

        return np.array(z).transpose()

    @abstractmethod
    def numericalSolution(self):
        pass

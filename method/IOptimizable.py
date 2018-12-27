import matplotlib.pylab as plt
import numpy as np
from py_expression_eval import Parser
from abc import ABC, ABCMeta, abstractmethod
from sympy.plotting import plot3d
from sympy import *

class optimizable(ABC):
    __metaclass__ = ABCMeta

    # Input data
    targetExpression = 'x^2+y^2'
    a = -2
    b = 2
    c = -1
    d = 1
    eps = 0.1
    maxN = 0

    # Output data
    N = 0
    x_ = 0
    Q_ = 0

    def __init__(self, targetFunction, a, b, c, d, eps, maxN):
        self.targetExpression = targetFunction
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.eps = eps
        self.maxN = maxN

        self.expression = Parser().parse(self.targetExpression)


    def printExpression(self):
        print('Q(x,y) = ' + self.targetExpression)


    def Q(self, x, y):
        return self.expression.evaluate({'x': x, 'y': y})


    def initPlot(self, plotName, X, Y):
        x, y = np.meshgrid(X, Y)
        z = []
        for i in X:
            tmp = []
            for j in Y:
                tmp.append(self.Q(i, j))
            z.append(tmp)
        z = np.array(z)

        # Create plot
        plt.figure(plotName)
        contours = plt.contour(x, y, z, 15)  # Линии уровня целевой функции (последний аргумент - количество линий)
        plt.clabel(contours, inline=True, fontsize=8)  # Значение уровня на линиях (последний аргумент - размер шрифта)

        return plt


    def showFunction3D(self):
        x, y = symbols('x y')
        plot3d(self.targetExpression, (x, self.a, self.b), (y, self.c, self.d))


    def showFunction2D(self):
        density = 50
        X = np.linspace(self.a, self.b, density)
        Y = np.linspace(self.c, self.d, density)

        self.initPlot(self.targetExpression, X, Y).show(self.targetExpression)

    def showMin2D(self):
        density = 50
        X = np.linspace(self.a, self.b, density)
        Y = np.linspace(self.c, self.d, density)

        newPlot = self.initPlot('Min valuu', X, Y)
        newPlot.plot(self.x_.x, self.x_.y, self.Q_, 'rs', label='optimum')
        newPlot.show()


    def showReference(self):
        print('->Input:')
        print('--->Q(x,y) = ' + self.targetExpression)
        print('--->[a, b] = [', self.a, ',', self.b, ']')
        print('--->[c, d] = [', self.c, ',', self.d, ']')
        print('--->eps = ', self.eps)

        print('->Output:')
        print('--->Iterations: ', self.N)
        print('--->x* = (%3.f, %3.f)' % (self.x_.x, self.x_.y))
        print('--->Q(x*) = %3.f' % self.Q_)


    @abstractmethod
    def numericalSolution(self):
        pass

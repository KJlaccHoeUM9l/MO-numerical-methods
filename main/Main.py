from method.IOptimizable import optimizable
from method.divisionByThree import divisionByThree

import numpy as np


if __name__ == '__main__':
    targetFunction = 'x^2+y^2'
    #targetFunction = '3*(x^2+y)^2+(x^2-1)^2'
    a = -2
    b = 2
    c = -1
    d = 1
    eps = 0.001
    maxN = 100
    method = divisionByThree(targetFunction, a, b, c, d, eps, maxN)

    method.printExpression()
    method.numericalSolution()
    method.showReference()
    #method.showMin2D()
    #method.showFunction3D()
    #method.showFunction2D()
    method.animation2D()


















# """
# A simple example of an animated plot
# """
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
#
# fig, ax = plt.subplots()
#
# x = np.arange(0, 2*np.pi, 0.01)
# line, = ax.plot(x, np.sin(x))
#
#
# def animate(i):
#     line.set_ydata(np.sin(x + i/10.0))  # update the data
#     return line,
#
#
# # Init only required for blitting to give a clean slate.
# def init():
#     line.set_ydata(np.ma.array(x, mask=True))
#     return line,
#
# ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
#                               interval=25, blit=True)
# plt.show()

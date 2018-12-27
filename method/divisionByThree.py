from method.IOptimizable import optimizable
import math


class divisionByThree(optimizable):
    K = []
    L = 0.5

    # Override
    def numericalSolution(self):
        P = rectangle(point(self.a, self.d), point(self.b, self.c))
        Px, Py, Pz = self.getThreeRectangles(P)

        self.K.append(self.getTuple(Px))
        self.K.append(self.getTuple(Py))
        self.K.append(self.getTuple(Pz))

        Kt, Q_eval, Q_min, x_min = self.iterationOfSearch(self.K)

        self.K.remove(Kt)

        i = 0
        while (abs(Q_min - Q_eval) > self.eps and i < 100):
            Pt = Kt.__getitem__(0)
            Px, Py, Pz = self.getThreeRectangles(Pt)

            self.K.append(self.getTuple(Px))
            self.K.append((Py, Kt.__getitem__(1), Kt.__getitem__(1) - self.L * (Py.getDiam() / 2.0)))
            self.K.append(self.getTuple(Pz))

            Kt, Q_eval, Q_min, x_min = self.iterationOfSearch(self.K)

            i += 1

        # Reference data
        self.Q_ = float(Q_min)
        self.x_ = x_min
        self.N = i


    def iterationOfSearch(self, K):
        Kt = self.K[0]
        Q_eval = self.K[0].__getitem__(2)
        Q_min = self.K[0].__getitem__(1)
        x_min = self.K[0].__getitem__(0).center

        for Ki in self.K:
            if Ki.__getitem__(2) < Q_eval:
                Kt = Ki
                Q_eval = Ki.__getitem__(2)
            if Ki.__getitem__(1) < Q_min:
                Q_min = Ki.__getitem__(1)
                x_min = Ki.__getitem__(0).center

        return Kt, Q_eval, Q_min, x_min



    def getThreeRectangles(self, P):
        if (P.width >= P.height):
            x0 = P.leftUp.x
            x3 = P.rightDown.x
            step = (x3 - x0) / 3.0
            x1 = x0 + step
            x2 = x0 + 2 * step

            yUp = P.leftUp.y
            yDown = P.rightDown.y

            Px = rectangle(point(x0, yUp), point(x1, yDown))
            Py = rectangle(point(x1, yUp), point(x2, yDown))
            Pz = rectangle(point(x2, yUp), point(x3, yDown))
        else:
            y0 = P.rightDown.y
            y3 = P.leftUp.y
            step = (y3 - y0) / 3.0
            y1 = y0 + step
            y2 = y0 + 2 * step

            xLeft = P.leftUp.x
            xRight = P.rightDown.x

            Px = rectangle(point(xLeft, y1), point(xRight, y0))
            Py = rectangle(point(xLeft, y2), point(xRight, y1))
            Pz = rectangle(point(xLeft, y3), point(xRight, y2))

        return Px, Py, Pz

    def getTuple(self, P):
        Q = self.Q(P.center.x, P.center.y)
        Q_ = Q - self.L * (P.getDiam() / 2.0)

        return (P, Q, Q_)


# Helper classes
class point:
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


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

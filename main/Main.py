from method.divisionByThree import divisionByThree

EXIT = 0
BACK = 9
INPUT_FUNC = 1
INPUT_BORDERS = 2
INPUT_L = 3
USE_METHOD = 4
SHOW_3D = 5
SHOW_2D = 6
ANIMATION = 7
REFERENCE = 8

if __name__ == '__main__':
    targetFunction = '(x-1)^2+y^2'
    a = -2
    b = 2
    c = -1
    d = 1
    eps = 0.001
    maxN = 1000
    L = 0.2

    select = -1
    while select != EXIT:
        print('SELECT ACTION:')
        print(INPUT_FUNC, ' - input target function')
        print(INPUT_BORDERS, ' - set conditions')
        print(INPUT_L, ' - set L')
        print(USE_METHOD, ' - get numerical solution')
        print(EXIT, ' - EXIT')
        select = int(input('Your action: '))

        if select == INPUT_FUNC:
            print('Enter target function: like x^2+y^2')
            targetFunction = input('--->Q(x,y) = ')
        elif select == INPUT_BORDERS:
            a = float(input('Enter left boundary on OX[a]: '))
            b = float(input('Enter right boundary on OX[b]: '))
            c = float(input('Enter down boundary on OY[c]: '))
            c = float(input('Enter up boundary on OY[d]: '))
            eps = float(input('Enter precision of method[eps]: '))
            maxN = int(input('Enter max quantity of steps[N]: '))
        elif select == INPUT_L:
            L = float(input('Enter Lipschitz constant[L]: '))
        elif select == USE_METHOD:
            method = divisionByThree(targetFunction, a, b, c, d, eps, maxN, L)
            method.numericalSolution()

            act = 47
            while act != BACK:
                print('SELECT ACTION:')
                print(SHOW_3D, ' - show target function 3D')
                print(SHOW_2D, ' - show level lines and solution')
                print(ANIMATION, ' - show animation')
                print(REFERENCE, ' - show reference')
                print(BACK, ' - BACK')
                act = int(input('Your choose: '))

                if act == SHOW_3D:
                    method.showFunction3D()
                elif act == SHOW_2D:
                    method.showMin2D()
                elif act == ANIMATION:
                    method.animation2D()
                elif act == REFERENCE:
                    print('********************** REFERENCE **********************')
                    method.showReference()
                    print('*******************************************************')

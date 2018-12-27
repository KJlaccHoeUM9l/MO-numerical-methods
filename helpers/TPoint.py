class point:
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    
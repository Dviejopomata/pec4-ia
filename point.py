import math


def slope(dx, dy):
    return (dy / dx) if dx else None


class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

    def halfway(self, target):
        midx = (self.x + target.x) / 2
        midy = (self.y + target.y) / 2
        return Point(midx, midy)

    def distance(self, target):
        dx = target.x - self.x
        dy = target.y - self.y
        return (dx * dx + dy * dy) ** 0.5

    def reflect_x(self):
        return Point(-self.x, self.y)

    def reflect_y(self):
        return Point(self.x, -self.y)

    def reflect_x_y(self):
        return Point(-self.x, -self.y)

    def slope_from_origin(self):
        return slope(self.x, self.y)

    def slope(self, target):
        return slope(target.x - self.x, target.y - self.y)

    def y_int(self, target):  # <= here's the magic
        return self.y - self.slope(target) * self.x

    def same_y(self, target):
        return self.m(target) == 0

    def m(self, target):
        n = (target.y - self.y) / (target.x - self.x)
        return n
        # return math.degrees(math.atan(n))

    def line_equation(self, target):
        slope = self.slope(target)

        y_int = self.y_int(target)
        if y_int < 0:
            y_int = -y_int
            sign = '-'
        else:
            sign = '+'

        return 'y = {:0.2f}x {} {:0.2f}'.format(slope, sign, y_int)

    def line_equation_solve(self, target, x):
        slope = self.slope(target)

        y_int = self.y_int(target)
        return (slope * x) + y_int
        # 'y = {:0.2f}x {} {:0.2f}'.format(slope, sign, y_int)
        # y = slope * x + y_int
        # x = y - y_int / slope

    def line_equation_solve_y(self, target, y):
        slope = self.slope(target)
        if slope == 0:
            return None
        y_int = self.y_int(target)
        return (y - y_int) / slope
        # return (slope * x) + y_int

    def line_function(self, target):
        slope = self.slope(target)
        y_int = self.y_int(target)

        def fn(x):
            return slope * x + y_int

        return fn

    def equal(self, point):
        return self.x == point.x and self.y == point.y

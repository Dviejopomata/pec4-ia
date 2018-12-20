import math

import pandas as pd
import numpy as np
from numpy import ones, vstack
from numpy.linalg import lstsq
from matplotlib import pyplot as plt

from point import Point

VL = 'vl'
L = 'l'
M = 'm'
H = 'h'
VH = 'vh'

var_a_vl = [(-5, 1), (-5, 1), (-4, 1), (0, 0)]
var_a_l = [(-5, 0), (-1, 1), (-1, 1), (1, 0)]
var_a_m = [(-1, 0), (1, 1), (1, 1), (2, 0)]
var_a_h = [(0, 0), (2, 1), (2, 1), (4, 0)]
var_a_vh = [(1, 0), (3, 1), (5, 1), (5, 1)]
var_a = {
    'title': 'VarA',
    'points': {
        VL: var_a_vl,
        L: var_a_l,
        M: var_a_m,
        H: var_a_h,
        VH: var_a_vh,
    },
    'colors': {
        'vl': 'blue',
        'l': 'pink',
        'm': 'red',
        'h': 'black',
        'vh': 'gray'
    }
}

var_b_vl = [(0, 1), (0, 1), (4, 1), (8, 0)]
var_b_l = [(0, 0), (8, 1), (8, 1), (10, 0)]
var_b_m = [(4, 0), (10, 1), (10, 1), (12, 0)]
var_b_h = [(8, 0), (14, 1), (14, 1), (20, 0)]
var_b_vh = [(10, 0), (20, 1), (20, 1), (20, 1)]

var_b = {
    'title': 'VarB',
    'points': {
        'vl': var_b_vl,
        'l': var_b_l,
        'm': var_b_m,
        'h': var_b_h,
        'vh': var_b_vh,
    },
    'colors': {
        'vl': 'blue',
        'l': 'pink',
        'm': 'red',
        'h': 'black',
        'vh': 'gray'
    }
}
var_c_l = [(0, 1), (0, 1), (1, 1), (4, 0)]
var_c_m = [(2, 0), (4, 1), (4, 1), (9, 0)]
var_c_h = [(5, 0), (7, 1), (8, 1), (10, 0)]

var_c = {
    'l': var_c_l,
    'm': var_c_m,
    'h': var_c_h,
}

var_d_l = [(0, 1), (0, 1), (1, 1), (3, 0)]
var_d_m = [(1, 0), (4, 1), (4, 1), (10, 0)]
var_d_h = [(5, 0), (8, 1), (10, 1), (10, 1)]

var_d = {
    'l': var_d_l,
    'm': var_d_m,
    'h': var_d_h,
}

var_out_vl = [(0, 0), (2, 1), (2, 1), (3, 0)]
var_out_l = [(2, 0), (3, 1), (3, 1), (5, 0)]
var_out_m = [(4, 0), (5, 1), (5, 1), (9, 0)]
var_out_h = [(6, 0), (7, 1), (7, 1), (10, 0)]
var_out_vh = [(7, 0), (9, 1), (10, 1), (10, 1)]

var_out = {
    'vl': var_out_vl,
    'l': var_out_l,
    'm': var_out_m,
    'h': var_out_h,
    'vh': var_out_vh,
}


def get_line(points):
    formulas = []
    (prev_x, prev_y) = points[0]
    for point in points:
        (x, y) = point
        p1 = Point(prev_x, prev_y)
        p2 = Point(x, y)
        if p1.equal(p2):
            continue
        eq = p1.line_equation(p2)

        prev_x = x
        prev_y = y
        formulas.append((p1, p2, eq))
    return formulas


print(get_line(var_a_vl))
print(get_line(var_a_l))
print(get_line(var_a_m))
print(get_line(var_a_h))
print(get_line(var_a_vh))

print(get_line(var_b_vl))
print(get_line(var_b_l))
print(get_line(var_out_vl))
print(get_line(var_out_l))

# print(get_line(var_a_l, var_a_l_y))
# print(get_line(var_b_vl))


a = Point(-4., 1.)
b = Point(0., 0.)

# print(a)  # => (2.0, 2.0)
# print(repr(b))  # => Point(4.0, 3.0)
# print(a.halfway(b))  # => (3.0, 2.5)
#
# print(a.slope(b))  # => 0.5
# print(a.y_int(b))  # => 1.0
# print(a.line_equation(b))  # => y = 0.5x + 1.0

# line = a.line_function(b)
# print(line(x=6.))  # => 4.0

# def linear_equation(p1, p2):
#     # points = [(1,5),(3,4)]
#     points = [p1, p2]
#     x_coords, y_coords = zip(*points)
#     A = vstack([x_coords, ones(len(x_coords))]).T
#     m, c = lstsq(A, y_coords)[0]
#     print("Line Solution is y = {m}x + {c}".format(m=m, c=c))
#
#
# from decimal import Decimal
#
#
# def lin_equ(l1, l2):
#     # line encoded as l=(x,y)
#     m = Decimal((l2[1] - l1[1])) / Decimal(l2[0] - l1[0])
#     c = (l2[1] - (m * l2[0]))
#     return m, c
#
#
# linear_equation((-4, 1), (0, 0))
# print(lin_equ((-4, 1), (0, 0)))
#
#

# print(np.random.randn(1000))
# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ddd = [{'x': -5, 'y': 1}, {'x': -4, 'y': 1}, {'x': 0, 'y': 0}]
df = pd.DataFrame(ddd)
df = df.cumsum()


# df.plot(x='x', y='y')
# plt.scatter(df['x'], df['y'])
# plt.plot(df['x'], df['y'])


# def get_color(var, pname):


def plot_var(item):
    lines = item['points']
    colors = item['colors']
    print(lines, colors)
    for key, value in lines.items():

        x = []
        y = []
        for l in get_line(value):
            (p1, p2, formula) = l
            x.extend([p1.x, p2.x])
            y.extend([p1.y, p2.y])
            halfpoint = p1.halfway(p2)
            m = p1.slope(p2)
            if m != 0:
                x___ = halfpoint.x
                y___ = halfpoint.y
                l2 = np.array([x___, y___]) / 2
                angles = np.array((30,)) if m > 0 else np.array((-30,))
                print(m, l2, angles, p1, p2, formula)
                trans_angle = plt.gca().transData.transform_angles(angles, l2.reshape((1, 2)))[0]
                plt.text(x___, y___, formula, rotation=trans_angle, rotation_mode='anchor')
        plt.plot(x, y, '.-', label=key, color=colors[key])
    plt.grid(True)
    # plt.xticks(np.arange(-5, 5, 1))
    plt.legend(loc='best')
    plt.title(item['title'])
    plt.show()


def plot_bar(var):
    line = get_line(var)

    for p in line:
        (p1, p2, formula) = p
        # print(p1, p2, formula)
        plt.plot([p1.x, p2.x], [p1.y, p2.y], 'ro-', color='green')


plot_var(var_a)
# plot_var(var_b)

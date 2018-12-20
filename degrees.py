import math
from math import acos
from math import sqrt
from math import pi
import pandas as pd
import numpy as np


def length(v):
    return sqrt(v[0] ** 2 + v[1] ** 2)


def dot_product(v, w):
    return v[0] * w[0] + v[1] * w[1]


def determinant(v, w):
    return v[0] * w[1] - v[1] * w[0]


def inner_angle(v, w):
    cosx = dot_product(v, w) / (length(v) * length(w))
    rad = acos(cosx)  # in radians
    return rad * 180 / pi  # returns degrees


def angle_clockwise(A, B):
    inner = inner_angle(A, B)
    det = determinant(A, B)
    if det < 0:  # this is a property of the det. If the det < 0 then B is clockwise of A
        return inner
    else:  # if the det > 0 then A is immediately clockwise of B
        return 360 - inner


x = [-4, 1]
y = [0, 0]

# print(angle_clockwise(x, y))
# print(inner_angle(x, y))

# x = np.array([-1, +1, +1, -1])
# y = np.array([-1, -1, +1, +1])
# x = np.array([-4, 0])
# y = np.array([1, 0])
# d = np.arctan2(y, x) * 180 / np.pi
# print(d)

rad = math.atan2(0 - 1, 0 - (-4))
degree = math.degrees(rad)
print(degree)

import matplotlib.pyplot as plt
import numpy as np

# Plot diagonal line (45 degrees)
h = plt.plot(np.arange(0, 30, 2), np.arange(0, 30, 2))

# set limits so that it no longer looks on screen to be 45 degrees
plt.xlim([-10, 20])

# Locations to plot text
l1 = np.array((1, 1))
l2 = np.array((5, 5))

# Rotate angle
angle = 45
trans_angle = plt.gca().transData.transform_angles(np.array((45,)), l2.reshape((1, 2)))[0]

x = np.array([1, 20])
y = np.array([1, 15])

# Plot text
# th1 = plt.text(l1[0], l1[1], 'text not rotated correctly', fontsize=16,
#                rotation=angle, rotation_mode='anchor')
# th2 = plt.text(l2[0], l2[1], 'text rotated correctly', fontsize=16,
#                rotation=trans_angle, rotation_mode='anchor')

trans_angle2 = plt.gca().transData.transform_angles(np.array((45,)), y.reshape((1, 2)))[0]

l3 = np.array([x[1] - x[0], y[1] - y[0]]) / 3
print(l3)
th2 = plt.text(l3[0], l3[1], 'text rotated correctly over my line', fontsize=16, rotation=trans_angle2,
               rotation_mode='anchor')

plt.plot(x, y, '.-', label='Linea')

plt.show()

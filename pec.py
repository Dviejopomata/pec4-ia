import base64
import io
import json
import math

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import savefig

from point import Point

VL = 'VL'
L = 'L'
M = 'M'
H = 'H'
VH = 'VH'

default_colors = {
    VL: 'blue',
    L: 'pink',
    M: 'red',
    H: 'black',
    VH: 'gray'
}

var_a_vl = [(-5, 1), (-5, 1), (-4, 1), (0, 0)]
var_a_l = [(-5, 0), (-1, 1), (-1, 1), (1, 0)]
var_a_m = [(-1, 0), (1, 1), (1, 1), (2, 0)]
var_a_h = [(0, 0), (2, 1), (2, 1), (4, 0)]
var_a_vh = [(1, 0), (3, 1), (5, 1), (5, 1)]
var_a = {
    'title': 'VarA',
    'multiplier_y': 7,
    'points': {
        VL: var_a_vl,
        L: var_a_l,
        M: var_a_m,
        H: var_a_h,
        VH: var_a_vh,
    },
    'colors': default_colors
}

var_b_vl = [(0, 1), (0, 1), (4, 1), (8, 0)]
var_b_l = [(0, 0), (8, 1), (8, 1), (10, 0)]
var_b_m = [(4, 0), (10, 1), (10, 1), (12, 0)]
var_b_h = [(8, 0), (14, 1), (14, 1), (20, 0)]
var_b_vh = [(10, 0), (20, 1), (20, 1), (20, 1)]

var_b = {
    'title': 'VarB',
    'multiplier_y': 14,
    'points': {
        VL: var_b_vl,
        L: var_b_l,
        M: var_b_m,
        H: var_b_h,
        VH: var_b_vh,
    },
    'colors': default_colors
}
var_c_l = [(0, 1), (0, 1), (1, 1), (4, 0)]
var_c_m = [(2, 0), (4, 1), (4, 1), (9, 0)]
var_c_h = [(5, 0), (7, 1), (8, 1), (10, 0)]

var_c = {
    'title': 'VarC',
    'multiplier_y': 8,
    'points': {
        L: var_c_l,
        M: var_c_m,
        H: var_c_h,
    },
    'colors': default_colors
}

var_d_l = [(0, 1), (0, 1), (1, 1), (3, 0)]
var_d_m = [(1, 0), (4, 1), (4, 1), (10, 0)]
var_d_h = [(5, 0), (8, 1), (10, 1), (10, 1)]

var_d = {
    'title': 'VarD',
    'multiplier_y': 8,
    'points': {
        L: var_d_l,
        M: var_d_m,
        H: var_d_h,
    },
    'colors': default_colors
}

var_out_vl = [(0, 0), (2, 1), (2, 1), (3, 0)]
var_out_l = [(2, 0), (3, 1), (3, 1), (5, 0)]
var_out_m = [(4, 0), (5, 1), (5, 1), (9, 0)]
var_out_h = [(6, 0), (7, 1), (7, 1), (10, 0)]
var_out_vh = [(7, 0), (9, 1), (10, 1), (10, 1)]

var_out = {
    'title': 'OutB1, Out',
    'multiplier_y': 8,
    'points': {
        VL: var_out_vl,
        L: var_out_l,
        M: var_out_m,
        H: var_out_h,
        VH: var_out_vh,
    },
    'colors': default_colors
}


def get_formulas(points):
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


ddd = [{'x': -5, 'y': 1}, {'x': -4, 'y': 1}, {'x': 0, 'y': 0}]
df = pd.DataFrame(ddd)
df = df.cumsum()


def plot_var(item):
    lines = item['points']
    colors = item['colors']
    for key, value in lines.items():

        x = []
        y = []
        line = get_formulas(value)
        for l in line:
            (p1, p2, formula) = l
            x.extend([p1.x, p2.x])
            y.extend([p1.y, p2.y])

        for l in line:
            (p1, p2, formula) = l
            halfpoint = p1.halfway(p2)
            m = p1.slope(p2)
            multipler_y = item['multiplier_y']
            rad = math.atan2((p2.y - p1.y) * multipler_y, p2.x - p1.x)
            degree = math.degrees(rad)
            rotation = degree
            if m != 0:
                x___ = halfpoint.x
                y___ = halfpoint.y + 0.05
                print(rotation, formula)
                plt.text(x___, y___, formula, rotation=rotation, rotation_mode='anchor')
        plt.plot(x, y, '.-', label=key, color=colors[key])
    plt.grid(True)
    # plt.xticks(np.arange(min_x, max_x, 1))
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.title(item['title'])


def plot_bar(var):
    line = get_formulas(var)

    for p in line:
        (p1, p2, formula) = p
        # print(p1, p2, formula)
        plt.plot([p1.x, p2.x], [p1.y, p2.y], 'ro-', color='green')


variables = [var_a, var_b, var_c, var_d, var_out]


def ej1():
    data = {
        'variables': []
    }
    for variable in variables:
        plot_var(variable)
        my_stringIObytes = io.BytesIO()
        plt.savefig(my_stringIObytes, format='png')
        my_stringIObytes.seek(0)
        imagen = base64.b64encode(my_stringIObytes.read())
        data['variables'].append({'imagen': imagen.decode('utf-8')})
        # savefig("tmp/%s.png" % variable['title'], bbox_inches='tight')
        plt.show()
    return data


def ej1_json():
    return ej1()


bloque_b1_metadata = ['VarA', 'VarB', 'OutB1']

bloque_b1 = [
    (VL, 'AND', VL, VL),
    (VL, 'AND', L, VL),
    (VL, 'AND', M, VL),
    (VL, 'AND', H, L),
    (VL, 'AND', VH, M),
    (L, 'AND', VL, L),
    (L, 'AND', L, L),
    (L, 'AND', M, M),
    (L, 'AND', H, M),
    (L, 'AND', VH, H),
    (M, 'AND', VL, M),
    (M, 'AND', L, M),
    (M, 'AND', M, M),
    (M, 'AND', H, M),
    (M, 'AND', VH, H),
    (H, 'AND', VL, H),
    (H, 'AND', L, H),
    (H, 'AND', M, H),
    (H, 'AND', H, H),
    (H, 'AND', VH, VH),
    (VH, 'AND', VL, H),
    (VH, 'AND', L, H),
    (VH, 'AND', M, H),
    (VH, 'AND', H, VH),
    (VH, 'AND', VH, VH),
]
bloque_b2_metadata = ['OutB1', 'VarC', 'VarD', 'Out']
bloque_b2 = [
    (VL, 'AND', L, 'AND', L, VL),
    (VL, 'AND', L, 'AND', M, VL),
    (VL, 'AND', L, 'AND', H, M),
    (VL, 'AND', M, 'AND', L, VL),
    (VL, 'AND', M, 'AND', M, VL),
    (VL, 'AND', M, 'AND', H, M),
    (VL, 'AND', H, 'AND', L, VL),
    (VL, 'AND', H, 'AND', M, M),
    (VL, 'AND', H, 'AND', H, H),
    (L, 'AND', L, 'AND', L, L),
    (L, 'AND', L, 'AND', M, L),
    (L, 'AND', L, 'AND', H, M),
    (L, 'AND', M, 'AND', L, L),
    (L, 'AND', M, 'AND', M, L),
    (L, 'AND', M, 'AND', H, M),
    (L, 'AND', H, 'AND', L, L),
    (L, 'AND', H, 'AND', M, L),
    (L, 'AND', H, 'AND', H, H),
    (M, 'AND', L, 'AND', L, M),
    (M, 'AND', L, 'AND', M, M),
    (M, 'AND', L, 'AND', H, M),
    (M, 'AND', M, 'AND', L, M),
    (M, 'AND', M, 'AND', M, M),
    (M, 'AND', M, 'AND', H, M),
    (M, 'AND', H, 'AND', L, M),
    (M, 'AND', H, 'AND', M, M),
    (M, 'AND', H, 'AND', H, M),
    (H, 'AND', L, 'AND', L, M),
    (H, 'AND', L, 'AND', M, M),
    (H, 'AND', L, 'AND', H, H),
    (H, 'AND', M, 'AND', L, M),
    (H, 'AND', M, 'AND', M, M),
    (H, 'AND', M, 'AND', H, H),
    (H, 'AND', H, 'AND', L, M),
    (H, 'AND', H, 'AND', M, M),
    (H, 'AND', H, 'AND', H, H),
    (VH, 'AND', L, 'AND', L, M),
    (VH, 'AND', L, 'AND', M, M),
    (VH, 'AND', L, 'AND', H, H),
    (VH, 'AND', M, 'AND', L, H),
    (VH, 'AND', M, 'AND', M, H),
    (VH, 'AND', M, 'AND', H, H),
    (VH, 'AND', H, 'AND', L, VH),
    (VH, 'AND', H, 'AND', M, VH),
    (VH, 'AND', H, 'AND', H, VH),
]


def get_max(points):
    x_arr = []
    y_arr = []
    for point in points:
        (x, y) = point
        x_arr.append(x)
        y_arr.append(y)
    return max(x_arr), min(x_arr), max(y_arr), min(y_arr)


def ej2_get_value(letra, var, x):
    points = var['points'][letra]
    formulas = get_formulas(points)
    y = None
    max_x, min_x, max_y, min_y = get_max(points)
    tmp_y = None
    for formula in formulas:
        (p1, p2, _) = formula
        if not p1.same_y(p2):
            tmp_y = p1.line_equation_solve(p2, x)
            if tmp_y is not None and (min_y <= tmp_y <= max_y):
                y = tmp_y
    if y is None:
        l = list(map(lambda i: i[2], formulas))
        print(l, var['title'], letra, x, tmp_y)
        return None
    return y


def format_number_bloque(n):
    if n is None or n == 0:
        return ""
    return '(%.2f)' % n


def get_bloque_b1_json(vars):
    (var_a_x, var_b_x, var_c_x, var_d_x) = vars
    success_rules = []
    i = 0
    for b in bloque_b1:
        (var_a_letra, AND, var_b_letra, var_outb1_letra) = b
        var_a_y = ej2_get_value(var_a_letra, var_a, var_a_x)
        var_b_y = ej2_get_value(var_b_letra, var_b, var_b_x)

        # return var_a_letra, AND, var_b_letra, var_outb1_letra
        # if var_a_y is not None and var_b_y is not None:
        #     v = min(var_a_y, var_b_y)
        #     prev_v = success_rules.get(var_outb1_letra)
        #     if (prev_v is not None and v > prev_v) or prev_v is None:
        #         success_rules[var_outb1_letra] = v
        var_outb1_y = None
        results = [var_a_y, var_b_y]
        print_out = [result for result in results if result is not None and result != 0]
        if len(print_out) == 2:
            var_outb1_y = min(var_a_y, var_b_y)
        success_rules.append({
            'n': f'{i:02}',
            'vara': '%s %s' % (var_a_letra, format_number_bloque(var_a_y)),
            'varb': '%s %s' % (var_b_letra, format_number_bloque(var_b_y)),
            'outb1': '%s %s' % (var_outb1_letra, format_number_bloque(var_outb1_y)),
        })
        i += 1
    return success_rules


def get_bloque_b1(vars):
    (var_a_x, var_b_x, var_c_x, var_d_x) = vars
    success_rules = {}
    for b in bloque_b1:
        (var_a_letra, _, var_b_letra, var_outb1_letra) = b
        var_a_y = ej2_get_value(var_a_letra, var_a, var_a_x)
        var_b_y = ej2_get_value(var_b_letra, var_b, var_b_x)
        if var_a_y is not None and var_b_y is not None:
            v = min(var_a_y, var_b_y)
            prev_v = success_rules.get(var_outb1_letra)
            if (prev_v is not None and v > prev_v) or prev_v is None:
                success_rules[var_outb1_letra] = v

    return success_rules


def get_bloque_b2_json(vars, b1):
    (var_a_x, var_b_x, var_c_x, var_d_x) = vars
    success_rules = []
    i = 0
    for b in bloque_b2:
        (var_outb1_letra, _, var_c_letra, _, var_d_letra, var_out_letra) = b
        var_c_y = ej2_get_value(var_c_letra, var_c, var_c_x)
        var_d_y = ej2_get_value(var_d_letra, var_d, var_d_x)
        var_outb1_y = b1.get(var_outb1_letra, None)
        var_out_letra_y = None
        results = [var_c_y, var_d_y, var_outb1_y]
        print_out = [result for result in results if result is not None and result != 0]
        if len(print_out) == 3:
            var_out_letra_y = min(var_c_y, var_d_y, var_outb1_y)
        success_rules.append({
            "n": f'{i:02}',
            'outb1': '%s %s' % (var_outb1_letra, format_number_bloque(var_outb1_y)),
            'varc': '%s %s' % (var_c_letra, format_number_bloque(var_c_y)),
            'vard': '%s %s' % (var_d_letra, format_number_bloque(var_d_y)),
            'out': '%s %s' % (var_out_letra, format_number_bloque(var_out_letra_y)),
        })
        i += 1
    return success_rules


def get_bloque_b2(vars, b1):
    (var_a_x, var_b_x, var_c_x, var_d_x) = vars
    success_rules = {}
    for b in bloque_b2:
        (var_outb1_letra, _, var_c_letra, _, var_d_letra, var_out_letra) = b
        var_c_y = ej2_get_value(var_c_letra, var_c, var_c_x)
        var_d_y = ej2_get_value(var_d_letra, var_d, var_d_x)
        var_outb1_y = b1.get(var_outb1_letra, None)
        if var_c_y is not None and var_d_y is not None and var_outb1_y is not None:
            v = min(var_c_y, var_d_y, var_outb1_y)
            # print(var_out_letra, v)
            prev_v = success_rules.get(var_out_letra)
            if (prev_v is not None and v > prev_v) or prev_v is None:
                success_rules[var_out_letra] = v

    return success_rules


def pecjson():
    data = ej1_json()
    b1 = get_bloque_b1(ej2_vars)
    data['ej2_bloque1'] = get_bloque_b1_json(ej2_vars)
    data['ej2_bloque2'] = get_bloque_b2_json(ej2_vars, b1)

    b1 = get_bloque_b1(ej3_vars)
    data['ej3_bloque1'] = get_bloque_b1_json(ej3_vars)
    data['ej3_bloque2'] = get_bloque_b2_json(ej3_vars, b1)
    print(data)
    return data


def ej2(vars):
    (var_a_x, var_b_x, var_c_x, var_d_x) = vars
    bloque_b1_success = get_bloque_b1(vars)


def ej3(vars):
    (vara, varb, varc, vard) = vars


ej2_vars = (0.5, 11, 6, 6)
ej3_vars = (2, 2, 4, 4)
if __name__ == '__main__':
    # rules = ej2(ej2_vars)
    # print(rules)
    f = open("./file.json", "w")
    data = pecjson()
    f.write(json.dumps(data, indent=4))
    f.close()

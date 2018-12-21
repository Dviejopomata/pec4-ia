import matplotlib.pyplot as plt
import numpy as np

import unittest
import numpy as np
import pec as pec
import sympy as sp


class TestStringMethods(unittest.TestCase):

    def test_ej2_get_value_when_none(self):
        y = pec.ej2_get_value(pec.VL, pec.var_a, 0.5)
        self.assertEqual(y, None)

    def test_ej2_get_value_when_true(self):
        y = pec.ej2_get_value(pec.M, pec.var_a, 0.5)
        print(y)
        self.assertEqual(y, 0.75)

    def test_ej2(self):
        b1 = pec.get_bloque_b1(pec.ej2_vars)
        print(b1)
        b2 = pec.get_bloque_b2(pec.ej2_vars, b1)
        print(b2)
        points = pec.var_out['points']
        items = points.items()
        colors = pec.var_out['colors']
        max_x, min_x, max_y, min_y = pec.get_max_dict(points)
        for letra, value in items:
            x = []
            y = []
            formulas = pec.get_formulas(value)
            vs = []
            v = b2.get(letra, None)
            for p1, p2, formula in formulas:
                x.extend([p1.x, p2.x])
                y.extend([p1.y, p2.y])
                if v is not None:
                    if not p1.same_y(p2):
                        v_tmp = p1.line_equation_solve_y(p2, v)
                        vs.append(v_tmp)
            if v is not None:
                plt.axhline(v, xmin=vs[0] / max_x, xmax=(vs[1] if len(vs) == 2 else 10) / max_x, color=colors[letra])
            plt.plot(x, y, '.-', label=letra, color=colors[letra])
        plt.margins(x=0, y=0)
        plt.show()

    def test_integrals_ej2(self):
        # points = pec.var_out['points']
        # for letra, value in points.items():
        #     if res_ej2.get(letra, None) is not None:
        #         formulas = pec.get_formulas(value)
        #         f1_p1, f1_p2, f1_formula = formulas[0]
        #         f2_p1, f2_p2, f2_formula = formulas[1]
        #         v = res_ej2.get(letra)
        #         f1_corte = f1_p1.line_equation_solve_y(f1_p2, v)
        #         f2_corte = f2_p1.line_equation_solve_y(f2_p2, v)
        #         print(v, f1_formula, f1_corte, f2_formula, f2_corte)
        x = sp.Symbol('x')

        def calculate_masa(functions):
            upper_side = 0
            lower_side = 0
            for func in functions:
                f, lower_bound, upper_bound = func
                upper_side = upper_side + sp.integrate(f * x, (x, lower_bound, upper_bound))
                lower_side = lower_side + sp.integrate(f, (x, lower_bound, upper_bound))
            print(upper_side, lower_side)
            masa = upper_side / lower_side
            return masa

        res_ej2 = {'M': 0.5, 'H': 0.25, 'VH': 0.10000000000000009}
        functions_ej2 = [
            ((x - 4), 4, 4.5),
            (res_ej2['M'], 4.5, 7),
            ((-0.25 * x + 2.25), 7, 8),
            (res_ej2['H'], 8, 9.25),
            ((-0.33 * x + 3.33), 9.25, 9.78),
            (res_ej2['VH'], 9.78, 10),
        ]

        masa_ej2 = calculate_masa(functions_ej2)
        print("masa_ej2", masa_ej2)

        res_ej3 = {'M': 0.25}
        functions_ej3 = [
            ((x - 4), 4, 4.25),
            (res_ej3['M'], 4.5, 8),
            ((-0.25 * x + 2.25), 8, 9),
        ]
        masa_ej3 = calculate_masa(functions_ej3)
        print("masa_ej3", masa_ej3)
        pass

    def test_ej3(self):
        print("EJ3")
        b1 = pec.get_bloque_b1(pec.ej3_vars)
        print(b1)
        b2 = pec.get_bloque_b2(pec.ej3_vars, b1)
        print(b2)
        points = pec.var_out['points']
        items = points.items()
        colors = pec.var_out['colors']
        max_x, min_x, max_y, min_y = pec.get_max_dict(points)
        for letra, value in items:
            x = []
            y = []
            formulas = pec.get_formulas(value)
            vs = []
            v = b2.get(letra, None)
            for p1, p2, formula in formulas:
                x.extend([p1.x, p2.x])
                y.extend([p1.y, p2.y])
                if v is not None:
                    if not p1.same_y(p2):
                        v_tmp = p1.line_equation_solve_y(p2, v)
                        vs.append(v_tmp)
            if v is not None:
                plt.axhline(v, xmin=vs[0] / max_x, xmax=(vs[1] if len(vs) == 2 else 10) / max_x, color=colors[letra])
            plt.plot(x, y, '.-', label=letra, color=colors[letra])
        plt.margins(x=0, y=0)
        plt.show()

    def test_integral(self):
        b = np.pi / 2
        a = 0
        n = 100
        x = np.linspace(a, b, n)
        fx = np.sin(x)
        area = np.sum(fx) * (b - a) / n
        print(area)
        x = sp.Symbol('x')
        # area = sp.integrate(3.0 * x ** 2 + 1, x)
        # print(area)
        # a = sp.integrate(sp.sin(3.0 * x), (x, 0, np.pi))
        a = sp.integrate(x * (x - 4), (x, 4, 4.5))
        print("sin area", a)

    def test_integral_plot2(self):
        # x = np.array(range(-10, 10))
        # plt.plot(x, y)
        # plt.fill_between(x, y, 3)
        # plt.show()

        def f(x):
            return x

        def g(x):
            return x ** 2

        def h(x):
            return 0.25 * x + 1.25

        x = np.linspace(0, 1, 100)
        plt.plot(x, f(x))
        plt.plot(x, h(x))
        plt.plot(x, g(x))
        plt.fill_between(x, f(x), g(x), label='X', color="grey", alpha=0.3, hatch='|')
        plt.fill_between(x, g(x), label='X^2', color="yellow", alpha=0.2, hatch='-')
        plt.fill_between(x, h(x), f(x), label='0.25x + 1.25', color="blue", alpha=0.1, hatch='\\')
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.show()

    def test_integral_plot(self):
        x = np.arange(0.0, 2, 0.01)
        y1 = np.sin(2 * np.pi * x)
        y2 = 1.2 * np.sin(4 * np.pi * x)
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)

        ax1.fill_between(x, 0, y1)
        ax1.set_ylabel('between y1 and 0')

        ax2.fill_between(x, y1, 1)
        ax2.set_ylabel('between y1 and 1')

        ax3.fill_between(x, y1, y2)
        ax3.set_ylabel('between y1 and y2')
        ax3.set_xlabel('x')
        plt.show()


if __name__ == '__main__':
    unittest.main()

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')
    #
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

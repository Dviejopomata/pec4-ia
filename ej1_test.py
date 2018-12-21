import unittest
import numpy as np
import pec as pec


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

    def test_ej3(self):
        print("EJ2")
        b1 = pec.get_bloque_b1(pec.ej2_vars)
        print(b1)
        b2 = pec.get_bloque_b2(pec.ej2_vars, b1)
        print(b2)
        for key, value in b2.items():
            print(key, value)
        print("EJ3")
        b1 = pec.get_bloque_b1(pec.ej3_vars)
        print(b1)
        b2 = pec.get_bloque_b2(pec.ej3_vars, b1)
        print(b2)


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

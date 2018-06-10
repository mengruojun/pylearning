import unittest
import Lib.copy as copy
from magic_cube import magic_cube as mc


class TestSortImplementations(unittest.TestCase):

    def setUp(self):
        self.mc = mc.MagicCube({
            'F': [' ', 'y', 'r', 'g', 'g', 'g', 'g', 'g', 'b', 'b'],
            'U': [' ', 'b', 'g', 'r', 'r', 'w', 'y', 'o', 'w', 'w'],
            'L': [' ', 'w', 'b', 'b', 'r', 'o', 'y', 'y', 'o', 'w'],
            'R': [' ', 'r', 'o', 'y', 'o', 'r', 'y', 'r', 'b', 'r'],
            'B': [' ', 'b', 'w', 'o', 'b', 'b', 'y', 'y', 'g', 'g'],
            'D': [' ', 'o', 'o', 'w', 'w', 'y', 'w', 'o', 'r', 'g']
        })

    def test_evaluate(self):
        temp_mc = mc.MagicCube({
            'F': [' ', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f'],
            'U': [' ', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'],
            'L': [' ', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l'],
            'R': [' ', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
            'B': [' ', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
            'D': [' ', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd']
        })
        print(temp_mc.evaluate())
        self.assertEqual(temp_mc.evaluate(), 20)
        temp_mc.f()
        print(temp_mc.evaluate())

    def test_f(self):
        self.mc.f()
        mc_f = {'F': [' ', 'g', 'g', 'y', 'b', 'g', 'r', 'b', 'g', 'g'],
                'U': [' ', 'b', 'g', 'r', 'r', 'w', 'y', 'w', 'y', 'b'],
                'L': [' ', 'w', 'b', 'o', 'r', 'o', 'o', 'y', 'o', 'w'],
                'R': [' ', 'o', 'o', 'y', 'w', 'r', 'y', 'w', 'b', 'r'],
                'B': [' ', 'b', 'w', 'o', 'b', 'b', 'y', 'y', 'g', 'g'],
                'D': [' ', 'r', 'o', 'r', 'w', 'y', 'w', 'o', 'r', 'g']}

        self.assertDictEqual(mc_f, self.mc.state)
        self.assertTrue(self.mc.evaluate(), 1)

    def test_f_a(self):
        old_mc = copy.deepcopy(self.mc.state)
        self.mc.f_a()
        self.mc.f()
        self.assertDictEqual(old_mc, self.mc.state)

    # F,L,U,
    def test_l(self):
        self.mc.l()
        mc_l = {'F': [' ', 'b', 'r', 'g', 'r', 'g', 'g', 'o', 'b', 'b'],
                'U': [' ', 'g', 'g', 'r', 'y', 'w', 'y', 'o', 'w', 'w'],
                'L': [' ', 'y', 'r', 'w', 'o', 'o', 'b', 'w', 'y', 'b'],
                'R': [' ', 'r', 'o', 'y', 'o', 'r', 'y', 'r', 'b', 'r'],
                'B': [' ', 'b', 'w', 'o', 'b', 'b', 'w', 'y', 'g', 'o'],
                'D': [' ', 'y', 'o', 'w', 'g', 'y', 'w', 'g', 'r', 'g']
                }
        self.assertDictEqual(mc_l, self.mc.state)

    def test_l_a(self):
        old_mc = copy.deepcopy(self.mc.state)
        self.mc.l_a()
        self.mc.l()
        self.assertDictEqual(old_mc, self.mc.state)

    def test_u(self):
        self.mc.u()
        mc_expected ={
            'F': [' ', 'r', 'o', 'y', 'g', 'g', 'g', 'g', 'b', 'b'],
            'U': [' ', 'o', 'r', 'b', 'w', 'w', 'g', 'w', 'y', 'r'],
            'L': [' ', 'y', 'r', 'g', 'r', 'o', 'y', 'y', 'o', 'w'],
            'R': [' ', 'b', 'w', 'o', 'o', 'r', 'y', 'r', 'b', 'r'],
            'B': [' ', 'w', 'b', 'b', 'b', 'b', 'y', 'y', 'g', 'g'],
            'D': [' ', 'o', 'o', 'w', 'w', 'y', 'w', 'o', 'r', 'g']
        }
        self.assertDictEqual(mc_expected, self.mc.state)

    def test_u_a(self):
        old_mc = copy.deepcopy(self.mc.state)
        self.mc.u_a()
        self.mc.u()
        self.assertDictEqual(old_mc, self.mc.state)

    #R,B,D
    def test_r(self):
        self.mc.r()
        mc_expected = {
            'F': [' ', 'y', 'r', 'w', 'g', 'g', 'w', 'g', 'b', 'g'],
            'U': [' ', 'b', 'g', 'g', 'r', 'w', 'g', 'o', 'w', 'b'],
            'L': [' ', 'w', 'b', 'b', 'r', 'o', 'y', 'y', 'o', 'w'],
            'R': [' ', 'r', 'o', 'r', 'b', 'r', 'o', 'r', 'y', 'y'],
            'B': [' ', 'w', 'w', 'o', 'y', 'b', 'y', 'r', 'g', 'g'],
            'D': [' ', 'o', 'o', 'y', 'w', 'y', 'b', 'o', 'r', 'b']
        }
        self.assertDictEqual(mc_expected, self.mc.state)

    def test_r_a(self):
        old_mc = copy.deepcopy(self.mc.state)
        self.mc.r_a()
        self.mc.r()
        self.assertDictEqual(old_mc, self.mc.state)

    def test_b(self):
        self.mc.b()
        mc_expected = {
            'F': [' ', 'y', 'r', 'g', 'g', 'g', 'g', 'g', 'b', 'b'],
            'U': [' ', 'y', 'y', 'r', 'r', 'w', 'y', 'o', 'w', 'w'],
            'L': [' ', 'r', 'b', 'b', 'g', 'o', 'y', 'b', 'o', 'w'],
            'R': [' ', 'r', 'o', 'g', 'o', 'r', 'r', 'r', 'b', 'o'],
            'B': [' ', 'y', 'b', 'b', 'g', 'b', 'w', 'g', 'y', 'o'],
            'D': [' ', 'o', 'o', 'w', 'w', 'y', 'w', 'w', 'r', 'y']
        }
        self.assertDictEqual(mc_expected, self.mc.state)

    def test_b_a(self):
        old_mc = copy.deepcopy(self.mc.state)
        self.mc.b_a()
        self.mc.b()
        self.assertDictEqual(old_mc, self.mc.state)

    def test_d(self):
        self.mc.d()
        mc_expected = {
            'F': [' ', 'y', 'r', 'g', 'g', 'g', 'g', 'y', 'o', 'w'],
            'U': [' ', 'b', 'g', 'r', 'r', 'w', 'y', 'o', 'w', 'w'],
            'L': [' ', 'w', 'b', 'b', 'r', 'o', 'y', 'y', 'g', 'g'],
            'R': [' ', 'r', 'o', 'y', 'o', 'r', 'y', 'g', 'b', 'b'],
            'B': [' ', 'b', 'w', 'o', 'b', 'b', 'y', 'r', 'b', 'r'],
            'D': [' ', 'o', 'w', 'o', 'r', 'y', 'o', 'g', 'w', 'w']
        }
        self.assertDictEqual(mc_expected, self.mc.state)

    def test_d_a(self):
        old_mc = copy.deepcopy(self.mc.state)
        self.mc.d_a()
        self.mc.d()
        self.assertDictEqual(old_mc, self.mc.state)

    def test_f_getattr(self):
        self.mc.run_one_oper('f')
        mc_f = {'F': [' ', 'g', 'g', 'y', 'b', 'g', 'r', 'b', 'g', 'g'],
                'U': [' ', 'b', 'g', 'r', 'r', 'w', 'y', 'w', 'y', 'b'],
                'L': [' ', 'w', 'b', 'o', 'r', 'o', 'o', 'y', 'o', 'w'],
                'R': [' ', 'o', 'o', 'y', 'w', 'r', 'y', 'w', 'b', 'r'],
                'B': [' ', 'b', 'w', 'o', 'b', 'b', 'y', 'y', 'g', 'g'],
                'D': [' ', 'r', 'o', 'r', 'w', 'y', 'w', 'o', 'r', 'g']}

        self.assertDictEqual(mc_f, self.mc.state)


if __name__ == '__main__':
    unittest.main()

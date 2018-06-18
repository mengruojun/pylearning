import copy as copy
import random
import logging
import time
import math


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')


"""
File magic_cube.py
Author: Ruojun Meng

"""


class MagicCube(object):
    """
    F: green  ['', 'y', 'r', 'g', 'g', 'g',' g', 'g','b','b']   === F[5] must be 'g'
    L: orange
    U: white
    R: red
    B: blue
    D: yellow


    """

    front = [
        [],
    ]

    def __init__(self, state):
        """
        :param state:
        state={
        'F' : ['y', 'r', 'g', 'g', 'g',' g', 'g','b','b']
        ....
        ....
        }
        """
        self.state = state
        self.U = state['U']
        self.F = state['F']
        self.L = state['L']
        self.R = state['R']
        self.B = state['B']
        self.D = state['D']

    """
    Turn Operations
    F,L,U,R,B,D  they are clockwise
    Fa,La,Ua,Ra,Ba,Da  they are anti-clockwise
    Fa=3*F and etc.
    """

    def f(self):
        self.clock_wise(self.F)
        temp1, temp2, temp3 = self.U[7], self.U[8], self.U[9]
        self.U[7], self.U[8], self.U[9] = self.L[9], self.L[6], self.L[3]
        self.L[9], self.L[6], self.L[3] = self.D[3], self.D[2], self.D[1]
        self.D[1], self.D[2], self.D[3] = self.R[7], self.R[4], self.R[1]
        self.R[7], self.R[4], self.R[1] = temp3, temp2, temp1

    def f_a(self):
        self.f()
        self.f()
        self.f()

    def l(self):
        self.clock_wise(self.L)
        temp1, temp4, temp7 = self.F[1], self.F[4], self.F[7]
        self.F[1], self.F[4], self.F[7] = self.U[1], self.U[4], self.U[7]
        self.U[1], self.U[4], self.U[7] = self.B[9], self.B[6], self.B[3]
        self.B[9], self.B[6], self.B[3] = self.D[1], self.D[4], self.D[7]
        self.D[1], self.D[4], self.D[7] = temp1, temp4, temp7

    def l_a(self):
        self.l()
        self.l()
        self.l()

    def u(self):
        self.clock_wise(self.U)
        temp1, temp2, temp3 = self.F[1], self.F[2], self.F[3]
        self.F[1], self.F[2], self.F[3] = self.R[1], self.R[2], self.R[3]
        self.R[1], self.R[2], self.R[3] = self.B[1], self.B[2], self.B[3]
        self.B[1], self.B[2], self.B[3] = self.L[1], self.L[2], self.L[3]
        self.L[1], self.L[2], self.L[3] = temp1, temp2, temp3

    def u_a(self):
        self.u()
        self.u()
        self.u()

    def r(self):
        self.clock_wise(self.R)
        temp3, temp6, temp9 = self.F[3], self.F[6], self.F[9]
        self.F[3], self.F[6], self.F[9] = self.D[3], self.D[6], self.D[9]
        self.D[3], self.D[6], self.D[9] = self.B[7], self.B[4], self.B[1]
        self.B[7], self.B[4], self.B[1] = self.U[3], self.U[6], self.U[9]
        self.U[3], self.U[6], self.U[9] = temp3, temp6, temp9

    def r_a(self):
        self.r()
        self.r()
        self.r()

    def b(self):
        self.clock_wise(self.B)
        temp3, temp2, temp1 = self.U[3], self.U[2], self.U[1]
        self.U[3], self.U[2], self.U[1] = self.R[9], self.R[6], self.R[3]
        self.R[9], self.R[6], self.R[3] = self.D[7], self.D[8], self.D[9]
        self.D[7], self.D[8], self.D[9] = self.L[1], self.L[4], self.L[7]
        self.L[1], self.L[4], self.L[7] = temp3, temp2, temp1

    def b_a(self):
        self.b()
        self.b()
        self.b()

    def d(self):
        self.clock_wise(self.D)
        temp7, temp8, temp9 = self.F[7], self.F[8], self.F[9]
        self.F[7], self.F[8], self.F[9] = self.L[7], self.L[8], self.L[9]
        self.L[7], self.L[8], self.L[9] = self.B[7], self.B[8], self.B[9]
        self.B[7], self.B[8], self.B[9] = self.R[7], self.R[8], self.R[9]
        self.R[7], self.R[8], self.R[9] = temp7, temp8, temp9

    def d_a(self):
        self.d()
        self.d()
        self.d()

    def clock_wise(self, arry):
        temp1, temp2, temp3 = arry[1], arry[2], arry[3]
        arry[1], arry[2], arry[3] = arry[7], arry[4], arry[1]
        arry[7], arry[4], arry[1] = arry[9], arry[8], arry[7]
        arry[9], arry[8], arry[7] = arry[3], arry[6], arry[9]
        arry[3], arry[6], arry[9] = temp1, temp2, temp3

    def print_state(self):
        for side in self.state:
            logging.info(side + ":" + str(self.state[side]))

    def simulate_annealing(self):
        solution = []
        T0 = 10
        d = 1 - 0.001
        Tk = 1e-3
        T = T0

        value = self.evaluate()

        i = 1

        while T > Tk:
            logging.info("Run times: " + str(i))
            i += 1

            oper = self.generate_ops()
            temp_mc = MagicCube(copy.deepcopy(self.state))
            [real_oper, new_value] = temp_mc.run_oper(oper, value)

            if (new_value < value) or (random.random() < math.exp((value - new_value) / T)):
                logging.info(
                    "accept the new operations. new value is" + str(new_value))
                self.run_oper(real_oper, value)
                solution.append(real_oper)

                temp_value = self.evaluate()
                assert temp_value == new_value

                value = new_value
                logging.info("value is: " + str(value))
                logging.info(solution)
                self.print_state()

            T *= d

        logging.info("Last state:")
        self.print_state()

        return solution

    def search_solution(self):
        solution = []
        value = self.evaluate()
        print("initial value: " + str(value))
        while value > 0:
            oper = self.generate_ops()
            temp_mc = MagicCube(copy.deepcopy(self.state))
            [real_oper, new_value] = temp_mc.run_oper(oper, value)
            if new_value < value:
                self.run_oper(real_oper, value)
                solution.append(real_oper)

                temp_value = self.evaluate()
                assert temp_value == new_value

                value = new_value
                logging.info("value downgrade: " + str(value))
                logging.info(solution)
                self.print_state()
                print()
                print()

            # else: # accept the new_value by a rate

        logging.info("Last state:")
        self.print_state()

        return solution



    def run_oper(self, oper, old_value):
        """
            run oper sequence, one step by one step
            For each step, evaluate the value. If the value is less than old_value, return it and its real oper

        """

        track = []
        real_oper = []
        for o in oper:
            real_oper.append(o)
            self.run_one_oper(o)
            value = self.evaluate()
            track.append([copy.deepcopy(real_oper), value])
            if value < old_value:
                break

        return track[-1]

    def run_sequence(self, oper):
        """
            run oper sequence, one step by one step
        """

        track = []
        real_oper = []
        for o in oper:
            real_oper.append(o)
            self.run_one_oper(o)
            value = self.evaluate()
            track.append([copy.deepcopy(real_oper), value])

        return track[-1]

    def run_one_oper(self, oper):
        getattr(self, oper)()

    @staticmethod
    def generate_ops(steps=20):
        operation_set = ['f', 'l', 'u', 'r', 'b', 'd',
                         'f_a', 'l_a', 'u_a', 'r_a', 'b_a', 'd_a']
        ops = []
        while steps > 0:
            steps -= 1
            ops.append(operation_set[random.randint(0, 11)])
        return ops

    """
    evaluate the value of the state
    This evaluation function seemly need to be included into individual solution classes
    """

    def evaluate(self):
        value = 20

        # upper level
        if self.F[1] == self.F[5] and self.U[7] == self.U[5] and self.L[3] == self.L[5]:
            value -= 1
        if self.F[2] == self.F[5] and self.U[8] == self.U[5]:
            value -= 1
        if self.F[3] == self.F[5] and self.U[9] == self.U[5] and self.R[1] == self.R[5]:
            value -= 1
        if self.U[4] == self.U[5] and self.L[2] == self.L[5]:
            value -= 1
        if self.U[6] == self.U[5] and self.R[2] == self.R[5]:
            value -= 1
        if self.U[1] == self.U[5] and self.L[1] == self.L[5] and self.B[3] == self.B[5]:
            value -= 1
        if self.U[2] == self.U[5] and self.B[2] == self.B[5]:
            value -= 1
        if self.U[3] == self.U[5] and self.R[3] == self.R[5] and self.B[1] == self.B[5]:
            value -= 1

        # mid level
        if self.F[4] == self.F[5] and self.L[6] == self.L[5]:
            value -= 1
        if self.F[6] == self.F[5] and self.R[4] == self.R[5]:
            value -= 1
        if self.L[4] == self.L[5] and self.B[6] == self.B[5]:
            value -= 1
        if self.B[4] == self.B[5] and self.R[6] == self.R[5]:
            value -= 1

        # bottom level
        if self.F[7] == self.F[5] and self.D[1] == self.D[5] and self.L[9] == self.L[5]:
            value -= 1
        if self.F[8] == self.F[5] and self.D[2] == self.D[5]:
            value -= 1
        if self.F[9] == self.F[5] and self.D[3] == self.D[5] and self.R[7] == self.R[5]:
            value -= 1
        if self.D[4] == self.D[5] and self.L[8] == self.L[5]:
            value -= 1
        if self.D[6] == self.D[5] and self.R[8] == self.R[5]:
            value -= 1
        if self.D[7] == self.D[5] and self.L[7] == self.L[5] and self.B[9] == self.B[5]:
            value -= 1
        if self.D[8] == self.D[5] and self.B[8] == self.B[5]:
            value -= 1
        if self.D[9] == self.D[5] and self.R[9] == self.R[5] and self.B[7] == self.B[5]:
            value -= 1

        return value


if __name__ == '__main__':
    test = MagicCube({
        'F': [' ', 'y', 'r', 'g', 'g', 'g', 'g', 'g', 'b', 'b'],
        'U': [' ', 'b', 'g', 'r', 'r', 'w', 'y', 'o', 'w', 'w'],
        'L': [' ', 'w', 'b', 'b', 'r', 'o', 'y', 'y', 'o', 'w'],
        'R': [' ', 'r', 'o', 'y', 'o', 'r', 'y', 'r', 'b', 'r'],
        'B': [' ', 'b', 'w', 'o', 'b', 'b', 'y', 'y', 'g', 'g'],
        'D': [' ', 'o', 'o', 'w', 'w', 'y', 'w', 'o', 'r', 'g']
    })
    logging.info(time.time())
    print(test.search_solution())
    #logging.info(test.simulate_annealing())
    logging.info(time.time())

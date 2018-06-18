import copy as copy
import logging
import time
import random
from magic_cube import MagicCube

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

"""
File magic_cube.py
Author: Ruojun Meng

"""


"""
evaluate the value of the state
This evaluation function seemly need to be included into individual solution classes
"""

def evaluate(self):
    value = 0

    # upper level
    if self.F[1] == self.F[5] and self.U[7] == self.U[5] and self.L[3] == self.L[5]:
        value += 1
    if self.F[2] == self.F[5] and self.U[8] == self.U[5]:
        value += 1
    if self.F[3] == self.F[5] and self.U[9] == self.U[5] and self.R[1] == self.R[5]:
        value += 1
    if self.U[4] == self.U[5] and self.L[2] == self.L[5]:
        value += 1
    if self.U[6] == self.U[5] and self.R[2] == self.R[5]:
        value += 1
    if self.U[1] == self.U[5] and self.L[1] == self.L[5] and self.B[3] == self.B[5]:
        value += 1
    if self.U[2] == self.U[5] and self.B[2] == self.B[5]:
        value += 1
    if self.U[3] == self.U[5] and self.R[3] == self.R[5] and self.B[1] == self.B[5]:
        value += 1

    # mid level
    if self.F[4] == self.F[5] and self.L[6] == self.L[5]:
        value += 10e3
    if self.F[6] == self.F[5] and self.R[4] == self.R[5]:
        value += 10e3
    if self.L[4] == self.L[5] and self.B[6] == self.B[5]:
        value += 10e3
    if self.B[4] == self.B[5] and self.R[6] == self.R[5]:
        value += 10e3

    # bottom level
    if self.F[7] == self.F[5] and self.D[1] == self.D[5] and self.L[9] == self.L[5]:
        value += 10e4
    if self.F[8] == self.F[5] and self.D[2] == self.D[5]:  #  底面十字
        value += 10e5
    if self.F[9] == self.F[5] and self.D[3] == self.D[5] and self.R[7] == self.R[5]:
        value += 10e4
    if self.D[4] == self.D[5] and self.L[8] == self.L[5]:   #  底面十字
        value += 10e5
    if self.D[6] == self.D[5] and self.R[8] == self.R[5]: #  底面十字
        value += 10e5
    if self.D[7] == self.D[5] and self.L[7] == self.L[5] and self.B[9] == self.B[5]:
        value += 10e4
    if self.D[8] == self.D[5] and self.B[8] == self.B[5]: #  底面十字
        value += 10e5
    if self.D[9] == self.D[5] and self.R[9] == self.R[5] and self.B[7] == self.B[5]:
        value += 10e4

    return value

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
        value = evaluate(self)
        track.append([copy.deepcopy(real_oper), value])
        if value > old_value:
            break

    return track[-1]


def search_solution_layer_by_layer(initial_status):
    solution = []
    value = evaluate(initial_status)
    print("initial value: " + str(value))
    while value > 0:

        steps = random.randint(1, 20)
        oper = initial_status.generate_ops(steps)

        temp_mc = MagicCube(copy.deepcopy(initial_status.state))
        [real_oper, new_value] = run_oper(temp_mc, oper, value)
        if new_value > value:
            run_oper(initial_status,real_oper, value)
            solution.append(real_oper)

            temp_value = evaluate(initial_status)
            assert temp_value == new_value

            value = new_value
            logging.info("value upgrade: " + str(value))
            logging.info(solution)
            initial_status.print_state()
            print()
            print()

            # else: # accept the new_value by a rate

    logging.info("Last state:")
    initial_status.print_state()

    return solution


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
    print(search_solution_layer_by_layer(test))
    logging.info(time.time())

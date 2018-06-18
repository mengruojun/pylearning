import copy as copy
import logging
import time

from magic_cube import MagicCube

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

"""
File magic_cube.py
Author: Ruojun Meng

"""


def search_solution(initial_status):
    solution = []
    value = initial_status.evaluate()
    print("initial value: " + str(value))
    while value > 0:
        oper = initial_status.generate_ops()

        temp_mc = MagicCube(copy.deepcopy(initial_status.state))
        [real_oper, new_value] = temp_mc.run_oper(oper, value)
        if new_value > value:
            initial_status.run_oper(real_oper, value)
            solution.append(real_oper)

            temp_value = initial_status.evaluate()
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
    print(search_solution(test))
    logging.info(time.time())

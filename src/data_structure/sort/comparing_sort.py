"""This file is to compare those implemented sort algorithm"""
""" compare  heap_sort, merge_sort and quick_sort for 1000, 10000, 100000, 1000000 input"""

import random
import logging
import time
import tableprint as tp

from data_strcture.sort import *


logging.basicConfig(level=logging.WARNING, format='%(asctime)s %(message)s')


def performance_test(sort_impl, N):
    arr = []
    for i in range(0, N):
        arr.append(random.random())

    logging.info("Start")
    start = time.time()
    sort_impl(arr)
    end = time.time()
    logging.info("End. Time is spent: " + str(end-start) + "seconds")
    return end-start


if __name__ == '__main__':
    length = [10000, 100000, 1000000]
    sort = [quick_sort.quick_sort, merge_sort.merge_sort, heap_sort.heap_sort]
    hearers = ["testtesttesttesttesttesttesttest"]
    for s in sort:
        hearers.append(s.__name__)
    data = []
    for l in length:
        l_result = [str(l)]
        data.append(l_result)
        for s in sort:
            l_result.append("{0:.2f}".format(performance_test(s, l)))

    tp.table(data, hearers)


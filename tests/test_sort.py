import unittest
from data_strcture.sort import *


class TestSortImplementations(unittest.TestCase):

    def test_QuickSort(self):
        self.assertListEqual([1, 2, 3, 4, 5], quick_sort.quick_sort([5, 4, 3, 2, 1]))
        self.assertListEqual([-100, 0, 0, 0, 1, 2, 3, 4, 5, 99],
                             quick_sort.quick_sort([99, -100, 0, 0, 0, 1, 2, 3, 4, 5]))

    def test_MergeSort(self):
        self.assertListEqual([1, 2, 3, 4, 5], merge_sort.merge_sort([5, 4, 3, 2, 1]))
        self.assertListEqual([-100, 0, 0, 0, 1, 2, 3, 4, 5, 99],
                             merge_sort.merge_sort([99, -100, 0, 0, 0, 1, 2, 3, 4, 5]))

    def test_HeapSort(self):
        self.assertListEqual([1, 2, 3, 4, 5], heap_sort.heap_sort([5, 4, 3, 2, 1]))
        self.assertListEqual([-100, 0, 0, 0, 1, 2, 3, 4, 5, 99],
                             heap_sort.heap_sort([99, -100, 0, 0, 0, 1, 2, 3, 4, 5]))

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()

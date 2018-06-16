import unittest
from src.data_structure.other import other


class TestOther(unittest.TestCase):
    def test_slowFib(self):
        self.assertEqual(1, other.fib(1))
        self.assertEqual(1, other.fib(2))
        self.assertEqual(2, other.fib(3))
        self.assertEqual(3, other.fib(4))
        self.assertEqual(5, other.fib(5))
        self.assertEqual(8, other.fib(6))
        self.assertEqual(6765, other.fib(20))
        self.assertEqual(10946, other.fib(21))
        self.assertEqual(17711, other.fib(22))
        self.assertEqual(9227465, other.fib(35))

    def test_fastFib(self):
        self.assertEqual(1, other.fast_fib(1))
        self.assertEqual(1, other.fast_fib(2))
        self.assertEqual(2, other.fast_fib(3))
        self.assertEqual(3, other.fast_fib(4))
        self.assertEqual(5, other.fast_fib(5))
        self.assertEqual(8, other.fast_fib(6))
        self.assertEqual(6765, other.fast_fib(20))
        self.assertEqual(10946, other.fast_fib(21))
        self.assertEqual(17711, other.fast_fib(22))
        self.assertEqual(9227465, other.fast_fib(35))
        self.assertEqual(354224848179261915075, other.fast_fib(100))


if __name__ == '__main__':
    unittest.main()

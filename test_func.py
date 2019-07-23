import unittest

from main import *

# inherit TestCase from unittest module


class TestFunc(unittest.TestCase):

    def test_func1(self):
        result = func1()
        self.assertEqual(result, True)

    def test_func2(self):
        result = func2()
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()

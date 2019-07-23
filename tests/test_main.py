import unittest

# from main import *
from my_package.main import func1, func2, func3


class TestFunc(unittest.TestCase):

    def test_main(self):
        result = func1()
        self.assertEqual(result, True)

    def test_func2(self):
        result = func2()
        self.assertEqual(result, False)

    def test_func3(self):
        result = func3()
        self.assertEqual(result, '123')


if __name__ == '__main__':

    unittest.main()

import unittest

from my_func import func

# inherit TestCase from unittest module


class TestFunc(unittest.TestCase):

    def test_whatever(self):
        result = func()
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()

import unittest

# from main import *
from my_package.main import func1


class TestFunc1(unittest.TestCase):

    def test_func1(self):
        result = func1()
        self.assertNotEqual(result, False)

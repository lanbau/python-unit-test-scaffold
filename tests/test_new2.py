import unittest

# from main import *
from my_package.main import func2


class TestFunc2(unittest.TestCase):

    def test_func2(self):
        result = func2()
        self.assertNotEqual(result, True)

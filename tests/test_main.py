import unittest

# from main import *
from my_package.func1 import func1


class TestFunc(unittest.TestCase):

    def test_main(self):
        result = func1()
        self.assertEqual(result, True)

    # def test_func2(self):
    #     result = func2()
    #     self.assertEqual(result, True)


print('nested')
print(__name__)

if __name__ == '__main__':

    unittest.main()

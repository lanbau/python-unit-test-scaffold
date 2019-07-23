import unittest

from my_func import func


class TestSum(unittest.TestCase):
    def test_list_int(self):
        result = func()
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()

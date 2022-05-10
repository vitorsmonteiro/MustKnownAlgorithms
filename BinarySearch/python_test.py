import unittest
import random
from binary_search import binary_search
from binary_search import generate_list


class TestBinarySearch(unittest.TestCase):

    def value_in_list(self):
        ordered_list = generate_list(100)
        target = target = int(100*random.random())
        binary_res = True if binary_search(ordered_list, target) is not False else False
        expected_res = target in ordered_list
        self.assertEqual(binary_res, expected_res, f"Should be {expected_res}")
        

if __name__ == '__main__':
    unittest.main()
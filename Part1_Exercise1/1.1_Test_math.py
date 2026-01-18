
import unittest
from mathexercise import add

class TestAddFunction(unittest.TestCase):
    # TODO:
    # - Write tests for:
    #   * adding two positive numbers
    #   * adding two negative numbers
    #   * adding a positive and a negative number
    # - Use assertEqual to check the results.
    # - Use clear method names, e.g. test_add_positive_numbers, etc.

    # write your tests here:
    pass
   
   class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -5), -7)

    def test_add_positive_and_negative_number(self):
        self.assertEqual(add(10, -3), 7)


if __name__ == "__main__":
    unittest.main()

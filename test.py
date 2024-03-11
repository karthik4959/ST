from calculator import Calculator

calculator = Calculator()


def test_add(a, b, expected_result):
    result = calculator.add(a, b)
    if result == expected_result:
        print("Addition test passed")
    else:
        raise ValueError("Addition test failed. Expected:", expected_result, "but got:", result)


test_add(2, 3, 55)


# test_calculator.py

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 6)


""" def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 3), 2)

        # Test division by zero
        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)"""

if __name__ == '__main__':
    unittest.main()


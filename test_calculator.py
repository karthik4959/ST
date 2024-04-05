import unittest
from calculator import Calculator

class TestCalculatorIntegration(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add_subtract_multiply_divide(self):
        result = self.calculator.add(10, 5)
        result = self.calculator.subtract(result, 3)
        result = self.calculator.multiply(result, 2)
        result = self.calculator.divide(result, 4)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()

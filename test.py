import unittest
from calculator import Calculator

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(10,5)

    def test_add(self):
        self.assertEqual(15, self.calculator.add())

    def test_minus(self):
        self.assertEqual(5, self.calculator.sub())

    def test_multiple(self):
        self.assertEqual(50, self.calculator.mul())

    def test_devide(self):
        self.assertEqual(2, self.calculator.div())

if __name__ == "__main__":
    unittest.main()

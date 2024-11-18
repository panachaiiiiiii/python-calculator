import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(2, 2), 4)
    def test_subtract(self):
         self.assertEqual(self.calc.subtract(4, 2), -2)
         self.assertEqual(self.calc.subtract(4, 6), 2)
    def test_multiply(self):
         self.assertEqual(self.calc.multiply(4, -2), -8)
         self.assertEqual(self.calc.multiply(2,2), 4)
    def test_divide(self):
         self.assertEqual(self.calc.divide(10,2), 5)
         self.assertEqual(self.calc.divide(8, 2), 4)
    def test_modulo(self):
         self.assertEqual(self.calc.modulo(5, 2), 1)
         self.assertEqual(self.calc.modulo(6, 4), 2)


         

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()
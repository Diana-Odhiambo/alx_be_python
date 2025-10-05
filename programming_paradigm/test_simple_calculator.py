import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test addition method."""
        self.assertEqual(self.calc.add(5, 2), 7)
        self.assertEqual(self.calc.add(-4, 6), 2)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Test subtraction method."""
        self.assertEqual(self.calc.subtract(8, 9), -1)
        self.assertEqual(self.calc.subtract(12, 10), 2)
        self.assertEqual(self.calc.subtract(-3, -3), 0)

    def test_multiply(self):
        """Test multiplication method."""
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertEqual(self.calc.multiply(6, 3), 18)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide(self):
        """Test division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        # Division by zero should return None (not raise an error)
        self.assertIsNone(self.calc.divide(2, 0))

if __name__ == '__main__':
    unittest.main()


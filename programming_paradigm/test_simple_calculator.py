import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(5, 2), 7)
        self.assertEqual(self.calc.add(-4, 6), 2)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(8, 9), -1)
        self.assertEqual(self.calc.subtract(12, 10), 2)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertEqual(self.calc.multiply(6, 3), 18)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        # When dividing by zero, it should return None (not raise an error)
        self.assertIsNone(self.calc.divide(10, 0))


if __name__ == '__main__':
    unittest.main()



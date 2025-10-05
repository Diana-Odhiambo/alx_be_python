import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_addittion(self):
        self.assertEqual(self.calc.add(5,2), 7)
        self.assertEqual(self.calc.add(-4,6),2)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(8,9), -1)
        self.assertEqual(self.calc.subtract(12,10), 2)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,2), 4)
        self.assertEqual(self.calc.multiply(6,3), 18)
    
    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(2, 0)
        self.assertEqual(self.calc.divide(10,2), 5)
        
    if __name__ == '__main__':
        unittest.main()
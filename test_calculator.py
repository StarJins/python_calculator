import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_mul(self):
        result = calculator.mul(1, 2)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
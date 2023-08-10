import unittest
from app import addition, substraction

class FirstUnittest(unittest.TestCase):
    def test_sum(self):
        num1 = 10
        num2 = 20
        result = addition(num1, num2)
        self.assertEqual(result, num1 + num2)
    
    def test_minus(self):
        num1 = 20
        num2 = 10
        result = substraction(num1, num2)
        self.assertEqual(result, num1 - num2)

if __name__ == "__main__":
    unittest.main()

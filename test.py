import unittest
from app import addition

class FirstUnittest(unittest.TestCase):
    def test_sum(self):
        num1 = 10
        num2 = 20
        result = addition(num1, num2)
        self.assertEqual(result, num2 + num1)

if __name__ == "__main__":
    unittest.main()

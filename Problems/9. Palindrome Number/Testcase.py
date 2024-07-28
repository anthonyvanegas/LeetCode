import unittest
from Solution import Solution

class TestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.solution = Solution()

    def test_example1(self):
        input = {
            'x': -10
        }
        output = False
        self.assertEqual(self.solution.isPalindrome(input['x']), output)

    def test_example2(self):
        input = {
            'x': 101
        }
        output = True
        self.assertEqual(self.solution.isPalindrome(input['x']), output)

    def test_example3(self):
        input = {
            'x': 11
        }
        output = True
        self.assertEqual(self.solution.isPalindrome(input['x']), output)

    def test_example4(self):
        input = {
            'x': 121
        }
        output = True
        self.assertEqual(self.solution.isPalindrome(input['x']), output)

if __name__ == '__main__':
    unittest.main()
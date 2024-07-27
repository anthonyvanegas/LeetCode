import unittest
from Solution import Solution

class TestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.solution = Solution()

    def test_example1(self):
        input = {
            'x': 10
        }
        output = False
        self.assertEqual(self.solution.isPalindrome(input['x']), output)

if __name__ == '__main__':
    unittest.main()
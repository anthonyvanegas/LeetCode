import unittest
from Solution import Solution

class TestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.solution = Solution()

    def test_example1(self):
        s = "I"
        o = 1
        self.assertEqual(self.solution.romanToInt(s), o)

    def test_example2(self):
        s = "II"
        o = 2
        self.assertEqual(self.solution.romanToInt(s), o)

    def test_example3(self):
        s = "LVIII"
        o = 58
        self.assertEqual(self.solution.romanToInt(s), o)

    def test_example4(self):
        s = "MCMXCIV"
        o = 1994
        self.assertEqual(self.solution.romanToInt(s), o)

if __name__ == '__main__':
    unittest.main()
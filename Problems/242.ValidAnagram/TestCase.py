import unittest
from Solution import Solution


class TestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.solution = Solution()

    def test_example1(self):
        input = {
                's': "anagram",
                't': "nagaram",
                }
        output = True
        self.assertEqual(
                self.solution.isAnagram(input['s'], input['t']),
                output,
                f"{input['s'], input['t']} - Test Case Failed")

    def test_example2(self):
        input = {
                's': "rat",
                't': "car",
                }
        output = False
        self.assertEqual(
                self.solution.isAnagram(input['s'], input['t']),
                output,
                f"{input['s'], input['t']} - Test Case Failed")


if __name__ == '__main__':
    unittest.main()


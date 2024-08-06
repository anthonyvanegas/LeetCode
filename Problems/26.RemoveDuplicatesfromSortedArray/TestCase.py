import unittest
from Solution import Solution


class TestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.solution = Solution()

    def test_example1(self):
        input = {
            "nums": [1, 1],
            }
        output = 1
        self.assertEqual(
                self.solution.removeDuplicates(input["nums"]),
                output,
                f"{input["nums"]} - Test Case Failed")

    def test_example2(self):
        input = {
            "nums": [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
            }
        output = 5
        self.assertEqual(
                self.solution.removeDuplicates(input["nums"]),
                output,
                f"{input["nums"]} - Test Case Failed")


if __name__ == '__main__':
    unittest.main()


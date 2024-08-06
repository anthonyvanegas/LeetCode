import unittest
from Solution import Solution


class TestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.solution = Solution()

    def test_example1(self):
        input = {
                'nums': [1, 1, 1, 2, 2, 3],
                'k': 2,
                }
        output = [1, 2]
        self.assertEqual(
                self.solution.topKFrequent(input['nums'], input['k']),
                output,
                f"{input['nums'], input['k']} - Test Case Failed")

    def test_example2(self):
        input = {
                'nums': [1],
                'k': 1,
                }
        output = [1]
        self.assertEqual(
                self.solution.topKFrequent(input['nums'], input['k']),
                output,
                f"{input['nums'], input['k']} - Test Case Failed")

    def test_example3(self):
        input = {
                'nums': [4, 1, -1, 2, -1, 2, 3],
                'k': 2,
                }
        output = [-1, 2]
        self.assertEqual(
                self.solution.topKFrequent(input['nums'], input['k']),
                output,
                f"{input['nums'], input['k']} - Test Case Failed")


if __name__ == '__main__':
    unittest.main()


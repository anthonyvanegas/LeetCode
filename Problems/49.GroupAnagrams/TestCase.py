import unittest
from Solution import Solution


class TestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.solution = Solution()

    def test_example1(self):
        input = {
                'strs': ["eat", "tea", "tan", "ate", "nat", "bat"],
                }
        output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        self.assertEqual(
                self.solution.groupAnagrams(input['strs']),
                output,
                f"{input['strs']} - Test Case Failed")


if __name__ == '__main__':
    unittest.main()


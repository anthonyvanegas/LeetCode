import unittest
from Solution import Solution

class TestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.solution = Solution()
    
    # Base Cases
    def test_example1(self):
        input = {
            'strs': ["flower"]
        }
        output =  "flower"
        self.assertEqual(self.solution.longestCommonPrefix(input['strs']), output, f"Test Case Failed: {input['strs']}")

    def test_example2(self):
        input = {
            'strs': ["flower", ""]
        }
        output =  ""
        self.assertEqual(self.solution.longestCommonPrefix(input['strs']), output, f"Test Case Failed: {input['strs']}")

    def test_example3(self):
        input = {
            'strs': ["flower","flow","flight"]
        }
        output = "fl"
        self.assertEqual(self.solution.longestCommonPrefix(input['strs']), output, f"Test Case Failed: {input['strs']}")

if __name__ == '__main__':
    unittest.main()
import unittest
from Solution import Solution

class TestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.solution = Solution()
    
    def test_example1(self):
        input = {
            's': "()"
        }
        output =  True
        self.assertEqual(self.solution.isValid(input['s']), output, f"Test Case Failed: {input['s']}")

    def test_example2(self):
        input = {
            's': "()[]{}"
        }
        output =  True
        self.assertEqual(self.solution.isValid(input['s']), output, f"Test Case Failed: {input['s']}")

    def test_example3(self):
        input = {
            's': "("
        }
        output =  False
        self.assertEqual(self.solution.isValid(input['s']), output, f"Test Case Failed: {input['s']}")

    def test_example4(self):
        input = {
            's': ")("
        }
        output =  False
        self.assertEqual(self.solution.isValid(input['s']), output, f"Test Case Failed: {input['s']}")

    def test_example5(self):
        input = {
            's': "()("
        }
        output =  False
        self.assertEqual(self.solution.isValid(input['s']), output, f"Test Case Failed: {input['s']}")

    def test_example6(self):
        input = {
            's': "({})("
        }
        output =  False
        self.assertEqual(self.solution.isValid(input['s']), output, f"Test Case Failed: {input['s']}")

if __name__ == '__main__':
    unittest.main()
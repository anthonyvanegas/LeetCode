import unittest
from Solution import Solution

class TestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.solution = Solution()

    def test_example1(self):
        input = {
            "nums": [2,7,11,15],
            "target": 9
        }
        output = [0,1]
        self.assertEqual(self.solution.twoSum(nums=input["nums"], target=input["target"]), output)

    def test_example2(self):
        input = {
            "nums": [3,2,4],
            "target": 6
        }
        output = [1,2]
        self.assertEqual(self.solution.twoSum(nums=input["nums"], target=input["target"]), output)


    def test_example3(self):
        input = {
            "nums": [3,3],
            "target": 6
        }
        output = [0,1]
        self.assertEqual(self.solution.twoSum(nums=input["nums"], target=input["target"]), output)

if __name__ == '__main__':
    unittest.main()

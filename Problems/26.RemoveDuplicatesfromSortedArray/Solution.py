from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ubound = len(nums) - 1
        print(ubound)
        for i in range(ubound, 1, -1):
            if nums[i] == nums[i-1]:
                nums[i] = "_"
        print(nums)
        return 1


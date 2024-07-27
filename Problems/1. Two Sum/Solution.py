from typing import List

# Submission Detail - https://leetcode.com/submissions/detail/1332183251/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[x] + nums[j] == target:
                    if x != j:
                        return [x,j]
        return 0

# Submission Detail - https://leetcode.com/submissions/detail/1345967507/
# Credit - https://www.youtube.com/watch?v=DEJAZBq0FDA

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 1
        for R in range(1, len(nums)):
            if nums[R] != nums[R - 1]:
                nums[L] = nums[R]
                L += 1
        return L

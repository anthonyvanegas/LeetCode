from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Check if greater
        #Then swap position after
        ubound = len(nums) - 1
        i = 0
        while i <= ubound - 1:
            pointer_1 = nums[i]
            j = i + 1
            while j <= ubound:
                pointer_2 = nums[j]
                if pointer_2 > pointer_1:
                    nums[i] = pointer_2
                    nums[j] = pointer_1
                    break
            i += 1
        return i + 1

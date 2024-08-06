# Submission Detail - https://leetcode.com/submissions/detail/1346014225/

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        sorted_map = sorted(list(enumerate(hash_map)), key=lambda x: x[1])
        hash_map = list(hash_map.keys())
        return [hash_map.keys()[nums[x][0]] for x in range(0, k)]

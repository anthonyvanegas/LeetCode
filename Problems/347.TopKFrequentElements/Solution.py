# Submission Detail - https://leetcode.com/submissions/detail/1347170954/

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        sorted_map = sorted(list(enumerate(hash_map.values())), key=lambda x: x[1], reverse=True)
        key_list= list(hash_map.keys())
        output = []
        for i in range(0, k):
            output.append(key_list[sorted_map[i][0]])
        return output
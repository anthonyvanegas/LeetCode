from typing import List

# Submission Detail - https://leetcode.com/submissions/detail/1339447744/ 
# Reference -  https://www.youtube.com/watch?v=0sWShKIJoo4

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cache = strs[0]
        
        for word in strs:
            i = 0
            while i < len(cache) and i < len(word) and word[i] == cache[i]:
                i += 1
            cache = word[:i]
        
        return cache
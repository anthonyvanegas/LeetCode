from typing import List

# Submission Detail - 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cache = strs[0]
        strs = strs[1:len(strs)]
        strs.sort(key=len)
        for word in strs:
            cache_len = len(cache)
            word_len = len(word)
            if cache_len == 0 or word_len == 0:
                return ""
            for i in range(0, len(cache)):
                if i+1 >= len(word) or cache[i] != word[i]:
                    if len(word) == 1:
                        cache = word
                    else:
                        cache = cache[0:i]
                    break
        return cache
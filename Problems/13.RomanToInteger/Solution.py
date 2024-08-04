# Submission Detail - https://leetcode.com/submissions/detail/1332183251/

class Solution:
    def romanToInt(self, s: str) -> int:
        hash_table = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        cache = 0
        for i in range(len(s) - 1, -1, -1):
            value = hash_table[s[i]]
            if value < cache:
                value = -value
            else:
                cache = value
            sum += value
        return sum

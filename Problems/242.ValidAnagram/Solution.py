# Submission Detail - https://leetcode.com/submissions/detail/1345993229/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        if s_len != t_len:
            return False

        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        for i in range(0, s_len):
            if s[i] != t[i]:
                return False

        return True

# Submission Detail - https://leetcode.com/submissions/detail/1339813701/

class Solution:
    def __init__(self):
        self.bracket_dict = {
            ')': '(',
            '}': '{',
            ']': '[',
            
        }
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False
        for b in s:
            if b not in self.bracket_dict:
                stack.append(b)
            elif len(stack) > 0:
                s_b = stack.pop()
                if s_b != self.bracket_dict[b]:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        
        return False
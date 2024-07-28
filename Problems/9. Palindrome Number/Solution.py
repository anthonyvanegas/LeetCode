# Submission Detail - https://leetcode.com/submissions/detail/1336664299/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        numStr = str(x)
        if numStr[0] != "-":
            upperIndex = len(numStr) - 1
            midIndex = (upperIndex + 2 - 1) // 2
            leftPart = numStr[0:midIndex]
            rightPart = numStr[midIndex+1:upperIndex+1]
            if len(numStr) % 2 != 0:
                rightPart = numStr[midIndex+1:upperIndex+1]
            else:
                rightPart = numStr[midIndex:upperIndex+1]
            if leftPart == rightPart[::-1]:
                return True
        return False
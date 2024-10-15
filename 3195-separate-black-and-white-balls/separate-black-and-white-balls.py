class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0
        i = len(s) - 1
        while i >= 0 and s[i] == "1":
            i -= 1
        j = i - 1
        while j >= 0:
            if s[j] == "1":
                res += i - j
                i -= 1
            j -= 1
        
        return res
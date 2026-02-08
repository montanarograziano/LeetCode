# Last updated: 08/02/2026, 14:28:11
class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        for c in s:
            if len(res) < 2 or not (res[-1] == c and res[-2] == c):
                res += c
        return res
            

        
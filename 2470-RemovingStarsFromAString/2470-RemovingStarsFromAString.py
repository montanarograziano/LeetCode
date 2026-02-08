# Last updated: 08/02/2026, 14:25:54
class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for c in s:
            if c != '*':
                res.append(c)
            else:
                res.pop()
        return "".join(res)
        
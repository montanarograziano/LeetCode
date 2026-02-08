# Last updated: 08/02/2026, 14:25:13
class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        for i in range(0, len(s) - 1, 2):
            if s[i] != s[i + 1]:
                res += 1
        return res
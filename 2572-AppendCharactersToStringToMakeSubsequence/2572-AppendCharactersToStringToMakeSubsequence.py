# Last updated: 08/02/2026, 14:25:42
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l, r = 0, 0
        while r < len(t) and l < len(s):
            if s[l] == t[r]:
                l += 1
                r += 1
            else:
                l += 1
        
        return len(t) - r
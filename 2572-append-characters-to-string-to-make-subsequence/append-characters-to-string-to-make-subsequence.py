class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l, r = 0, 0
        while r < len(t) and l < len(s):
            if s[l] == t[r]:
                l += 1
                r += 1
            else:
                l += 1
        
        if r == len(t):
            return 0
        else:
            return len(t) - r
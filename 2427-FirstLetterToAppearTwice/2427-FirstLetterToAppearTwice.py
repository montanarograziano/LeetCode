# Last updated: 08/02/2026, 14:25:58
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = {}
        for c in s:
            if c in d:
                return c
            else:
                d[c] = 1
            
        
        
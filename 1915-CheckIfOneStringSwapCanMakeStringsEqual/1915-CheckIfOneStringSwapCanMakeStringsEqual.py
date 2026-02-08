# Last updated: 08/02/2026, 14:27:11
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c1, c2 = Counter(s1), Counter(s2)
        if c1 != c2:
            return False
        
        diffs = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffs += 1
        return diffs == 0 or diffs == 2
        

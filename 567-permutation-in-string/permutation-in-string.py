class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_count = Counter(s1)
        i = 0
        l = len(s1)

        while i <= len(s2) - l:
            if Counter(s2[i:i+l]) == s1_count:
                return True
            i += 1
        
        return False
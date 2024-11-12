class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        l = s.split(' ')
        if len(l) != len(pattern):
            return False
        for a,b in zip(pattern, l):
            if a in d and d[a] != b:
                return False
            d[a] = b
        
        return len(d.keys()) == len(set(l))
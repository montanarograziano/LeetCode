class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        x = defaultdict(str)
        for a,b in zip(s, t):
            if not x[a]:
                x[a] = b
            elif x[a] != b:
                return False
        return len(x.keys()) == len(set(t))
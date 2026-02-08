# Last updated: 08/02/2026, 14:27:48
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        c = Counter(s)
        odd = sum(1 if c[ch] % 2 else 0 for ch in c)
        return odd <= k
        
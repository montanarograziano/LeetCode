# Last updated: 08/02/2026, 14:27:18
class Solution:
    def minPartitions(self, n: str) -> int:
        m = 0
        for c in n:
            m = max(int(c), m)
        return m
        
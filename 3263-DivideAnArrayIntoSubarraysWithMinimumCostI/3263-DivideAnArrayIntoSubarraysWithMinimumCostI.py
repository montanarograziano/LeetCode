# Last updated: 08/02/2026, 14:25:10
class Solution:
    def minimumCost(self, a: List[int]) -> int:
        return a[0]+sum(sorted(a[1:])[:2])

# Last updated: 08/02/2026, 14:27:21
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        w = [sum(x) for x in accounts]
        return max(w)
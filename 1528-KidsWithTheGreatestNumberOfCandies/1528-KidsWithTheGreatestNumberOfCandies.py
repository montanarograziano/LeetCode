# Last updated: 08/02/2026, 14:27:46
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        out = [True if c + extraCandies >= m else False for c in candies ]
        return out
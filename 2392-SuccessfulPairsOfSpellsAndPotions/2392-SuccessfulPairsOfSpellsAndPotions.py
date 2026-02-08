# Last updated: 08/02/2026, 14:26:02
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for s in spells:
            l, r = 0, len(potions) - 1
            idx = len(potions)

            while l <= r:
                mid = (l + r) // 2
                cur = potions[mid] * s
                if cur < success:
                    l = mid + 1
                else:
                    idx = mid
                    r = mid - 1
            res.append(len(potions) - idx)
        
        return res
                




        
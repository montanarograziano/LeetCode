# Last updated: 08/02/2026, 14:25:17
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m = max(nums)
        if len(nums) == m + 1:
            d = {}
            for n in nums:
                if n in d:
                    d[n] += 1
                else:
                     d[n] = 1
            for n in nums:
                if n == m:
                    if d[n] != 2:
                        return False
                else:
                    if d[n] != 1:
                        return False
            return True
        else:
            return False

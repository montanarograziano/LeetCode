# Last updated: 08/02/2026, 14:25:18
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        res = 1
        nums.sort()
        l = 0
        n = len(nums)
        for r in range(1, n):
            while nums[r] - nums[l] > 2 * k:
                l += 1
            res = max(res, r - l + 1)
        return res



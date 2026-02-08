# Last updated: 08/02/2026, 14:27:19
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        l, r = 0, len(nums) - 1
        while l < r:
            s = nums[l] + nums[r]
            if s == k:
                ans += 1
                l += 1
                r -= 1
            elif s < k:
                l += 1
            else:
                r -= 1


        return ans
        
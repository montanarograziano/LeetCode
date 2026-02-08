# Last updated: 08/02/2026, 14:26:15
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total = nums.count(1)
        n = len(nums)
        nums = nums + nums
        ones = cur = sum(nums[:total])
        for i in range(1, n):
            cur += nums[i + total -1]
            cur -= nums[i - 1]
            ones = max(ones, cur)

        return total - ones

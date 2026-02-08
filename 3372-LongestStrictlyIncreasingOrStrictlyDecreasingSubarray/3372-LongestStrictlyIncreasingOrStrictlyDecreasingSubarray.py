# Last updated: 08/02/2026, 14:25:06
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest, inc, dec = 1, 1, 1
        
        for i in range(1, len(nums)):
            inc = inc + 1 if nums[i] > nums[i - 1] else 1
            dec = dec + 1 if nums[i] < nums[i - 1] else 1
            longest = max(longest, inc, dec)
        
        return longest
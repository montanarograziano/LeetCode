class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        res = -1
        nums.sort()
        s = set(nums)
        for n in nums:
            cur = 1
            next_num = n ** 2
            while next_num in s:
                cur += 1
                res = max(res, cur)
                next_num = next_num ** 2
        
        return res



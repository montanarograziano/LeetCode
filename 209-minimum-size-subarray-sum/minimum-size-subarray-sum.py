class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        l, r = 0, 0
        cur = 0
        for n in nums:
            cur += n
            r += 1
            while cur >= target and l < r:
                res = min(res, r - l)
                cur -= nums[l]
                l += 1
        
        return res if res != float("inf") else 0
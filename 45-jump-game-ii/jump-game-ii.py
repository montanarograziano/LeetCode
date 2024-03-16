class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, len(nums) - 1
        while r > 0:
            if nums[l] + l >= r:
                res += 1
                r = l
                l = 0
            else:
                l += 1
        return res

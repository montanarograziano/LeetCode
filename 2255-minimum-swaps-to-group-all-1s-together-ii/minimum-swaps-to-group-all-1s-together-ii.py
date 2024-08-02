class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total = sum(1 if n == 1 else 0 for n in nums)
        n = len(nums)
        nums = nums + nums
        res = sum(1 if n == 0 else 0 for n in nums[:total])
        cur = res
        for i in range(1, n):
            if nums[i - 1] == 0:
                cur -= 1
            if nums[i + total - 1] == 0:
                cur += 1
            res = min(res, cur)

        return res

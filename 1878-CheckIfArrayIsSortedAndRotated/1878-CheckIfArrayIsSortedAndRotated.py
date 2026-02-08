# Last updated: 08/02/2026, 14:27:16
class Solution:
    def check(self, nums: List[int]) -> bool:
        inv = 0
        N = len(nums)
        for i in range(1, N):
            if nums[i] < nums[i - 1]:
                inv += 1

        if nums[0] < nums[N - 1]:
            inv += 1
        return inv <= 1

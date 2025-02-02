class Solution:
    def check(self, nums: List[int]) -> bool:
        inv = 0
        N = len(nums)
        for i in range(1, N):
            if nums[i] < nums[i - 1]:
                inv += 1
            if inv > 1 or (inv == 1 and nums[N - 1] > nums[0]):
                return False
        return True

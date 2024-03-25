class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        dp = set()
        dp.add(0)
        for i in range(len(nums)):
            if nums[i] > target:
                return False
            dpClone = dp.copy()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                if t + nums[i] < target:
                    dpClone.add(t + nums[i])
            dp = dpClone
        return False
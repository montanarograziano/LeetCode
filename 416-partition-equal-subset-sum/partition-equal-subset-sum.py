class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) / 2
        dp = set()
        dp.add(0)
        for i in range(len(nums) -1, -1, -1):
            next_dp = set()
            for n in dp:
                if (nums[i] + n) == target:
                    return True

                next_dp.add(nums[i] + n)
                next_dp.add(n)
            dp = next_dp
        
        return target in dp

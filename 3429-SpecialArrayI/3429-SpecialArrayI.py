# Last updated: 08/02/2026, 14:25:03
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
    
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                return False
        
        return True
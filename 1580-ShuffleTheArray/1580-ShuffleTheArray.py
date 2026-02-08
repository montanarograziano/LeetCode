# Last updated: 08/02/2026, 14:27:37
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        idx = n
        i = 0
        while idx < 2 * n:
            res.append(nums[i])
            res.append(nums[idx])
            i, idx = i + 1, idx + 1
        return res
            
        
        
# Last updated: 08/02/2026, 14:25:14
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d = Counter(nums)
        res = 0
        for n, c in d.items():
            if c == 1:
                return -1
            res += math.ceil(c / 3)
        return res
            
        
# Last updated: 08/02/2026, 14:28:12
class Solution:
    def kConcatenationMaxSum(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        
        def kadane(k):
            res = cur = 0
            for _ in range(k):
                for num in nums:
                    cur = max(cur + num, num)
                    res = max(res, cur)
            
            return res
        
        return (max(0, k - 2) * max(0, sum(nums)) + kadane(min(2, k))) % MOD
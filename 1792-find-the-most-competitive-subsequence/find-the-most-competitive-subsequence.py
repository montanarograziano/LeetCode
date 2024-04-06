class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        res = []
        res_len = 0
        l = len(nums)
        for i, n in enumerate(nums):
            while res and res[-1] > n and l - i - 1 >= k - res_len:
                res.pop(-1)
                res_len -= 1
            
            if res_len < k:
                res.append(n)
                res_len += 1
        
        return res

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def setbits(n):
            ans = 0
            while n != 0:
                n = n & (n-1)
                ans += 1
            return ans
        cur_min, cur_max = nums[0], nums[0]
        prev_max = float("-inf")

        for n in nums:
            if setbits(n) == setbits(cur_min):
                cur_min = min(cur_min, n)
                cur_max = max(cur_max, n)
            else:
                if cur_min < prev_max:
                    return False
                prev_max = cur_max
                cur_min, cur_max = n, n
        
        return not (cur_min < prev_max)
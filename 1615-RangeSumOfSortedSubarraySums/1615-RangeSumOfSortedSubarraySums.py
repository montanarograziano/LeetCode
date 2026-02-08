# Last updated: 08/02/2026, 14:27:33
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        sums = []
        for i in range(n):
            s = nums[i]
            sums.append(s)
            for j in range(i + 1, n):
                s += nums[j]
                sums.append(s)
        
        sums.sort()
        return sum(sums[left - 1 : right]) % MOD

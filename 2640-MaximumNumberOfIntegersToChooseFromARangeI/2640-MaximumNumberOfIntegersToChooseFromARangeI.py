# Last updated: 08/02/2026, 14:25:34
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set()
        for num in banned:
            if num <= n:
                banned_set.add(num)
        
        res = 0
        cur = 0
        for i in range(1, n + 1):
            if cur + i <= maxSum and i not in banned_set:
                res += 1
                cur += i
        return res
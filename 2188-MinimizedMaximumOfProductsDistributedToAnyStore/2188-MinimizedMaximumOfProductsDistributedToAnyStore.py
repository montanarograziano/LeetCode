# Last updated: 08/02/2026, 14:26:55
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def helper(mid):
            s = 0
            for q in quantities:
                s += math.ceil(q / mid)
            return s <= n

        l = 1
        r, res = max(quantities), max(quantities)
        
        while l < r:
            mid = l + (r - l) // 2
            cur = helper(mid)
            if cur:
                res = min(res, mid)
                r = mid
            else:
                l = mid + 1
        
        return res


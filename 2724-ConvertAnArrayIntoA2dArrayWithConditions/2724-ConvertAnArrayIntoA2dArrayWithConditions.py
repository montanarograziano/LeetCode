# Last updated: 08/02/2026, 14:25:25
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        m = []
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
            if len(m) == d[n] - 1:
                m.append([])
            m[d[n] - 1].append(n)
        
        return m
        



        
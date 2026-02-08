# Last updated: 08/02/2026, 14:25:57
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d1, d2 = {}, {}

        for i,row in enumerate(grid):
            d1[tuple(row)] = d1.get(tuple(row), 0) + 1

        for i,col in enumerate(zip(*grid)):
            d2[tuple(col)] = d2.get(tuple(col), 0) + 1
        
        d3 = set(d1) & set(d2)
        res = 0
        for k in d3:
            res += d1[k] * d2[k]
        return res

        
        

        
        

        
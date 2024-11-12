class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        res = [0] * len(queries)
        items.sort()
        queries = sorted([(q, i) for i, q in enumerate(queries)])
        max_b = 0
        j = 0
        for q, i in queries:
            while j < len(items) and items[j][0] <= q:
                max_b = max(max_b, items[j][1])
                j += 1
        
            res[i] = max_b
        
        return res



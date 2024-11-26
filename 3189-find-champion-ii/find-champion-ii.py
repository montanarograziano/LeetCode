class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 0
        res = -1
        visit = set([i for i in range(n)])
        for l, r in edges:
            if r in visit:
                visit.remove(r)
        
        return res if len(visit) > 1 else visit.pop()

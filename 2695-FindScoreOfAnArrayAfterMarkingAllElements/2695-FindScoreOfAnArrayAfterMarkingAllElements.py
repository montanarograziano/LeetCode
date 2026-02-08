# Last updated: 08/02/2026, 14:25:29
class Solution:
    def findScore(self, nums: List[int]) -> int:
        score, n = 0, len(nums)
        marked = 0
        m = [False] * n
        heap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(heap)
        while marked < n:
            el, i = heapq.heappop(heap)
            while m[i] == True:
                el, i = heapq.heappop(heap)
            score += el
            m[i] = True
            marked += 1
            for j in [i - 1, i + 1]:
                if j not in range(n):
                    continue
                if not m[j]:
                    m[j] = True
                    marked += 1
        return score
                    
            
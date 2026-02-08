# Last updated: 08/02/2026, 14:25:30
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-x for x in gifts]
        heapq.heapify(heap)
        for i in range(k):
            el = - heapq.heappop(heap)
            heapq.heappush(heap, - floor(sqrt(el)))
        return -sum(heap)



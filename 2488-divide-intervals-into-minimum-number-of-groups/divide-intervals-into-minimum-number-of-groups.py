class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        for l, r in intervals:
            if heap and l > heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, r)
        
        return len(heap)
        
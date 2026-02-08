# Last updated: 08/02/2026, 14:28:10
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        maxHeap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))
        
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                next_count, next_char = heapq.heappop(maxHeap)
                res += next_char
                next_count += 1
                if next_count:
                    heapq.heappush(maxHeap, (next_count, next_char))
            else:
                res += char
                count += 1
            
            if count:
                heapq.heappush(maxHeap, (count, char))
        
        return res


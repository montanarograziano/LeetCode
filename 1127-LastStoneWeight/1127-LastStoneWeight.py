# Last updated: 08/02/2026, 14:28:23
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        heapify(stones)
        while len(stones)>1:
            first=heappop(stones)*-1
            second=heappop(stones)*-1
            lastover=abs(first-second)
            heappush(stones,lastover*-1)

        return -stones[0]   
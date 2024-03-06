class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        fun = lambda x, y: (math.sqrt(x**2 + y**2), [x, y])

        dist = list(map(lambda p: fun(*p), points))

        heapq.heapify(dist)
        res = []
        for i in range(k):
            res.append(heapq.heappop(dist)[1])
        return res


        
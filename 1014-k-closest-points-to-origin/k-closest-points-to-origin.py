class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def fun(x, y):
            return (math.sqrt(x**2 + y**2), [x, y])

        dist = []
        for p in points:
            dist.append(fun(*p))

        heapq.heapify(dist)
        res = []
        for i in range(k):
            res.append(heapq.heappop(dist)[1])
        return res


        
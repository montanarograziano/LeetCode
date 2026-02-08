# Last updated: 08/02/2026, 14:26:01
class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [i for i in range(1, 1001)]
        self.set = set(self.heap)
        heapq.heapify(self.heap)
        

    def popSmallest(self) -> int:
        p = heapq.heappop(self.heap)
        self.set.remove(p)
        return p
        

    def addBack(self, num: int) -> None:
        if num in self.set:
            return
        self.set.add(num)
        heapq.heappush(self.heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
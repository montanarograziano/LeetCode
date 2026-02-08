# Last updated: 08/02/2026, 14:27:53
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        temp, res = [], []
        def num_bits(n: int):
            cnt = 0
            while n:
                n &= n - 1
                cnt += 1
            return cnt
        
        for n in arr:
            heapq.heappush(temp, (num_bits(n), n))
        while temp:
            res.append(heapq.heappop(temp)[1])
        return res
            
# Last updated: 08/02/2026, 14:28:04
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        tot = sum(nums)
        res = 0
        one_mod = []
        two_mod = []
        heapq.heapify(one_mod)
        heapq.heapify(two_mod)
        if tot % 3 == 0:
            return tot

        for n in nums:
            if n % 3 == 1:
                heapq.heappush(one_mod, n)
            elif n % 3 == 2:
                heapq.heappush(two_mod, n)
        
        if len(one_mod) < 2:
            one_mod += [float("inf")] * (2 - len(one_mod))

        if len(two_mod) < 2:
            two_mod += [float("inf")] * (2 - len(two_mod))
        
        if tot % 3 == 1:
            tot -= min(heapq.heappop(one_mod), heapq.heappop(two_mod) + heapq.heappop(two_mod))
        else:
            tot -= min(heapq.heappop(two_mod), heapq.heappop(one_mod) + heapq.heappop(one_mod))

        return tot
        


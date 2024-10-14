class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        queue = [-num for num in nums]
        heapq.heapify(queue)
        score = 0
        while k > 0:
            e = - heapq.heappop(queue)
            score += e
            heapq.heappush(queue, - math.ceil(e / 3))
            k -= 1
        
        return score
        
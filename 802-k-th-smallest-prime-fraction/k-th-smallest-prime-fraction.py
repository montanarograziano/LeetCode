class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        minHeap = []
        n = len(arr)
        for i in range(n - 1):
            heapq.heappush(minHeap, (arr[i] / arr[-1], i, n - 1))

        for _ in range(k - 1):
            _, numerator, denominator = heapq.heappop(minHeap)

            if denominator - 1 > numerator:
                heapq.heappush(
                    minHeap, (arr[numerator] / arr[denominator - 1], numerator, denominator - 1))

        _, i, j = heapq.heappop(minHeap)
        return [arr[i], arr[j]]
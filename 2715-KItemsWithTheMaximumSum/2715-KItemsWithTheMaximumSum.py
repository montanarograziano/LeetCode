# Last updated: 08/02/2026, 14:25:27
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes + numZeros:
            return min(numOnes, k)

        return numOnes - (k - numZeros - numOnes)


        
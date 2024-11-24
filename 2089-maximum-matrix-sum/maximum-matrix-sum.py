class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negatives = 0
        res = 0
        min_neg = float("inf")
        for row in matrix:
            for num in row:
                res += abs(num)
                min_neg = min(min_neg, abs(num))
                if num < 0:
                    negatives += 1
        
        return res - (2 * min_neg) if negatives & 1 else res

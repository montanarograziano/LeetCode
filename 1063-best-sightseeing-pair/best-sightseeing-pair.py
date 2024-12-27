class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        curmax = values[0] - 1
        for i in range(1, len(values)):
            res = max(res, values[i] + curmax)
            curmax = max(curmax - 1, values[i] - 1)
        return res

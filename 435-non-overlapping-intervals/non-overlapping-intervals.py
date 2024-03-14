class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        r = float("-inf")
        for i in sorted(intervals, key=lambda x:x[1]):
            if i[0] >= r:
                r = i[1]
            else:
                ans += 1
        return ans

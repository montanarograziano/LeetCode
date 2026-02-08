# Last updated: 08/02/2026, 14:28:02
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        sec = 0
        for i in range(len(points) - 1):
            curr = points[i]
            next_p = points[i + 1]
            sec += max(abs(curr[0] - next_p[0]), abs(curr[1] - next_p[1]))
        return sec

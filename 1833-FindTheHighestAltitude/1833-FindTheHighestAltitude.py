# Last updated: 08/02/2026, 14:27:17
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m, cur = 0, 0
        for n in gain:
            cur += n
            m = max(m, cur)
        return m

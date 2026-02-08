# Last updated: 08/02/2026, 14:27:32
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        between = high - low + 1
        
        if between & 1 == 1:
            if low & 1 == 1:
                return (between + 1) // 2
        
        return between // 2

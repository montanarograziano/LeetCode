# Last updated: 08/02/2026, 14:25:33
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even, odd, i = 0, 0, 0
        while n:
            if (n & 1) and (i & 1):
                odd += 1
            elif (n & 1):
                even += 1
            n >>= 1
            i += 1
        return [even, odd]


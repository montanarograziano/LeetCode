# Last updated: 08/02/2026, 14:25:51
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n * 2
        
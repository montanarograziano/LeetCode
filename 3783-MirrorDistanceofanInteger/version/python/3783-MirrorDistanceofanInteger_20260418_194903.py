# Last updated: 18/04/2026, 19:49:03
1class Solution:
2    def mirrorDistance(self, n: int) -> int:
3        def reverse(n):
4            res = 0
5            while n:
6                res = res * 10 + n % 10
7                n //= 10
8            return res
9        
10        return abs(n - reverse(n))
# Last updated: 03/03/2026, 20:18:52
1class Solution:
2    def findKthBit(self, n: int, k: int) -> str:
3        l = 2**n - 1
4        invert = False
5        while l > 1:
6            half = l // 2
7            if k <= half:
8                l = half
9            elif k > half + 1:
10                k = 1 + l - k
11                l = half
12                invert = not invert
13            else:
14                return "1" if not invert else "0"
15        
16        return "0" if not invert else "1"
17
18
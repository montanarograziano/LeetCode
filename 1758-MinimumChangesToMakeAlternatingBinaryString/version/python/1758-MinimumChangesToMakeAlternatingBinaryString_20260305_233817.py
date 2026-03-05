# Last updated: 05/03/2026, 23:38:17
1class Solution:
2    def minOperations(self, s: str) -> int:
3        start0 = 0
4        start1 = 0
5        
6        for i in range(len(s)):
7            if i % 2 == 0:
8                if s[i] == "0":
9                    start1 += 1
10                else:
11                    start0 += 1
12            else:
13                if s[i] == "1":
14                    start1 += 1
15                else:
16                    start0 += 1
17        
18        return min(start0, start1)
19
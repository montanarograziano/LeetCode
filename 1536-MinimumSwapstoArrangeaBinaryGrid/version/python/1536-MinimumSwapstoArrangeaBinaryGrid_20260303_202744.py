# Last updated: 03/03/2026, 20:27:44
1class Solution:
2    def minSwaps(self, grid: List[List[int]]) -> int:
3        n = len(grid)
4        pos = [-1] * n
5        for i in range(n):
6            for j in range(n - 1, -1, -1):
7                if grid[i][j] == 1:
8                    pos[i] = j
9                    break
10
11        ans = 0
12        for i in range(n):
13            k = -1
14            for j in range(i, n):
15                if pos[j] <= i:
16                    ans += j - i
17                    k = j
18                    break
19
20            if k != -1:
21                for j in range(k, i, -1):
22                    pos[j], pos[j - 1] = pos[j - 1], pos[j]
23            else:
24                return -1
25
26        return ans
27
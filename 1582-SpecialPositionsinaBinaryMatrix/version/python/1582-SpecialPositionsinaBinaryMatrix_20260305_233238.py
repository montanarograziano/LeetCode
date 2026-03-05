# Last updated: 05/03/2026, 23:32:38
1class Solution:
2    def numSpecial(self, mat: List[List[int]]) -> int:
3        m = len(mat)
4        n = len(mat[0])
5        row_count = [0] * m
6        col_count = [0] * n
7        
8        for row in range(m):
9            for col in range(n):
10                if mat[row][col] == 1:
11                    row_count[row] += 1
12                    col_count[col] += 1
13        
14        ans = 0
15        for row in range(m):
16            for col in range(n):
17                if mat[row][col] == 1:
18                    if row_count[row] == 1 and col_count[col] == 1:
19                        ans += 1
20
21        return ans
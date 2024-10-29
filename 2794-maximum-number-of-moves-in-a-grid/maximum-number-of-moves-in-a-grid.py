class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        cache = {}
        def dp(r, c):
            if (r,c) in cache:
                return cache[(r, c)]
            
            res = 0
            for dr, dc in [(r - 1, c + 1), (r, c + 1), (r + 1, c + 1)]:
                if dr in range(ROWS) and dc in range(COLS) and grid[r][c] < grid[dr][dc]:
                    res = max(res, 1 + dp(dr, dc)) 
            cache[(r, c)] = res
            return res
        
        return max(dp(row, 0) for row in range(ROWS))
        
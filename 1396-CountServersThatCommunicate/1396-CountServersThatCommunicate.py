# Last updated: 08/02/2026, 14:28:01
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        tot_rows = [0] * ROWS
        tot_cols = [0] * COLS
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    tot_rows[i] += 1
                    tot_cols[j] += 1  
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] and max(tot_rows[i], tot_cols[j]) > 1:
                    res += 1
        
        return res
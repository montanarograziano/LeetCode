class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        res = 0
        ROW, COL = len(grid) * 3, len(grid[0]) * 3
        new_grid = [[0] * COL  for _ in range(ROW)] 
        i = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                r2, c2 = r * 3, c * 3
                if grid[r][c] == '/':
                    new_grid[r2][c2 + 2] = 1
                    new_grid[r2 + 1][c2 + 1] = 1
                    new_grid[r2 + 2][c2] = 1
                elif grid[r][c] == '\\':
                    new_grid[r2][c2] = 1
                    new_grid[r2 + 1][c2 + 1] = 1
                    new_grid[r2 + 2][c2 +  2] = 1

        
        def dfs(r, c, visit):
            if (r < 0 or r == ROW or c < 0 or c == COL or (r, c) in visit or new_grid[r][c] == 1):
                return
            
            visit.add((r, c))
            neigh = [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]
            for nr, nc in neigh:
                dfs(nr, nc, visit)
            
        visit = set()

        for r in range(ROW):
            for c in range(COL):
                if new_grid[r][c] == 0 and (r, c) not in visit:
                    dfs(r, c, visit)
                    res += 1
        
        return res
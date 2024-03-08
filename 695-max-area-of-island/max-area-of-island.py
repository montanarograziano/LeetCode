class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        res = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visit:
                visit.add((r, c))
                dirs = [(1,0), (0,-1), (-1,0), (0, 1)]
                cur_area = 1
                for dr, dc in dirs:
                    row, col = r + dr, c + dc
                    cur_area += dfs(row, col)
                return cur_area
            
            return 0
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    current_area = dfs(r, c)
                    res = max(current_area, res)
                    
        
        return res
        
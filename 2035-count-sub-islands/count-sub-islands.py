class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        visit = set()
        islands = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r, c):
            if r in range(rows) and c in range(cols) and grid2[r][c] and (r, c) not in visit:
                visit.add((r, c))
                res = grid1[r][c] == 1
                for dr, dc in directions:
                    res = dfs(r + dr, c + dc) and res
                return res
            
            return True

        for r in range(rows):
            for c in range(cols): 
                if grid2[r][c] and (r, c) not in visit and dfs(r, c):
                    islands +=1 
        
        return islands
                
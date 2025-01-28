class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        res = 0
        waters = []
        visit = set()
        pr, pc = -1, -1
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or (r, c) in visit
                or grid[r][c] == 0
            ):
                return 0
            
            visit.add((r, c))
            res = grid[r][c]
            neigh = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in neigh:
                res += dfs(nr, nc)
            
            return res


        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))

        return res

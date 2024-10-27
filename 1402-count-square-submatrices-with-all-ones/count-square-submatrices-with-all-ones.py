class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}
        res = 0

        def helper(r, c):
            if r not in range(ROWS) or c not in range(COLS) or not matrix[r][c]:
                return 0
            
            if (r, c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)
                cache[(r, c)] = min(down, right, diag) + 1

            return cache[(r, c)]
        
        for r in range(ROWS):
            for c in range(COLS):
                res += helper(r, c)
        return sum(cache.values())
            

        
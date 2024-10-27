class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}

        def helper(r, c):
            if r not in range(ROWS) or c not in range(COLS):
                return 0
            
            if (r, c) not in cache:
                cache[(r, c)] = 0
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)
                if matrix[r][c] == 1:
                    cache[(r, c)] = min(down, right, diag) + 1

            return cache[(r, c)]
        
        helper(0, 0)
        return sum(cache.values())
            

        
# Last updated: 08/02/2026, 14:25:32
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])
        f_row = [0] * ROWS
        f_cols = [0] * COLS
        mapping = {}
        for r in range(ROWS):
            for c in range(COLS):
                mapping[mat[r][c]] = (r, c)
        
        for i, n in enumerate(arr):
            r, c = mapping[n]
            f_row[r] += 1
            f_cols[c] += 1
            if f_row[r] == COLS or f_cols[c] == ROWS:
                return i
        
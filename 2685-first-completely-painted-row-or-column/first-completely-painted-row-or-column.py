class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        max_row = 0
        max_col = 0
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
            max_row = max(max_row, f_row[r])
            max_col =  max(max_col, f_cols[c])
            if max_row == COLS or max_col == ROWS:
                return i
        
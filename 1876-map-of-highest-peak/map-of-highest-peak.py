class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(isWater), len(isWater[0])
        q = deque()
        res = [[-1] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c]:
                    q.append((r, c))
                    res[r][c] = 0       
        while q:
            r, c = q.popleft()
            h = res[r][c]
            
            for dr, dc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if dr < 0 or dr == ROWS or dc < 0 or dc == COLS or res[dr][dc] != -1:
                    continue
                q.append((dr, dc))
                res[dr][dc] = h + 1
        
        return res
                
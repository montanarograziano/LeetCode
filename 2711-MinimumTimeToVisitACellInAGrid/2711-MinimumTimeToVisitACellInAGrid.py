# Last updated: 08/02/2026, 14:25:27
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if min(grid[0][1], grid[1][0]) > 1:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        pq = [(0, 0, 0)] # time, row, col, cur_time
        visit = set()
        visit.add((0, 0))
        while pq:
            time, row, col = heapq.heappop(pq)
            if (row, col) == (ROWS - 1, COLS - 1):
                return time
            
            neig = [(row, col + 1), (row, col - 1), (row - 1, col), (row + 1, col)]
            for nr, nc in neig:
                if (nr, nc) in visit or nr < 0 or nr == ROWS or nc < 0 or nc == COLS:
                    continue
                wait = 0
                if abs(grid[nr][nc] - time) % 2 == 0:
                    wait = 1
                next_time = max(grid[nr][nc] + wait, time + 1)
                heapq.heappush(pq, (next_time, nr, nc))
                visit.add((nr, nc))
        
        return -1
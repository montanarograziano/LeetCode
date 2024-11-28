class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        min_heap = [(0, 0, 0)] # (obstacles, r, c)
        visit = set([(0, 0)])
        
        while min_heap:
            obstacles, r, c = heapq.heappop(min_heap)
            if (r, c) == (ROWS - 1, COLS - 1):
                return obstacles

            neigh = [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]
            for dr, dc in neigh:
                if (dr, dc) in visit or dr == ROWS or dr < 0 or dc == COLS or dc < 0:
                    continue
                
                heapq.heappush(min_heap, (obstacles + grid[dr][dc], dr, dc))
                visit.add((dr, dc))
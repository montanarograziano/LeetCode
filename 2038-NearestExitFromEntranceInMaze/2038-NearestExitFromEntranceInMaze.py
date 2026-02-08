# Last updated: 08/02/2026, 14:27:03
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze) - 1
        n = len(maze[0]) - 1

        queue = collections.deque()
        queue.append((entrance[0], entrance[1], 0))
        visited = set()
        visited.add((entrance[0], entrance[1]))

        while queue:
            for _ in range(len(queue)):
                r, c, level = queue.popleft()

                if [r, c] != entrance:
                    if r == 0 or r == m or c == 0 or c == n:
                        return level

                for nr, nc in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
                    if 0 <= nr <= m and 0 <= nc <= n and (nr, nc) not in visited and maze[nr][nc] == '.':
                        queue.append((nr, nc, level + 1))
                        visited.add((nr, nc))

        return -1
        
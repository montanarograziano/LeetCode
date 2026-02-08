# Last updated: 08/02/2026, 14:24:57
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[i + 1] for i in range(n)]
        def sp():
            q = deque()
            q.append((0, 0))
            visited = set()
            visited.add((0, 0))
            while q:
                cur, length = q.popleft()
                if cur == n - 1:
                    return length
                for nei in adj[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, length + 1))

        res = []
        for src, dst in queries:
            adj[src].append(dst)
            res.append(sp())

        return res
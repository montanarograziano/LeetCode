# Last updated: 08/02/2026, 14:27:38
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        connections = {(a,b) for a,b in connections}
        edges = {i: [] for i in range(n)}
        visited = set()
        changes = 0
        # Fill the adjacent
        for a,b in connections:
            edges[a].append(b)
            edges[b].append(a)
        
        # Try to traverse bfs
        q = deque()
        q.append(0)
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                adj = edges[cur]
                for node in adj:
                    if node not in visited:
                        if (cur, node) in connections:
                            changes += 1

                        q.append(node)
                visited.add(cur)
        
        return changes
                


        
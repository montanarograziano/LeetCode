class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = 0
        adj = defaultdict(list)
        for i, j, time in times:
            adj[i].append([time, j])
        
        q = [[0, k]]
        visited = set()
        while q:
            w1, n1 = heapq.heappop(q)
            if n1 in visited:
                continue

            visited.add(n1)
            res = max(res, w1)
            for w2, n2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(q, (w2 + w1, n2))

        return res if len(visited) == n else -1



        

        

        


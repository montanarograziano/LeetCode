# Last updated: 08/02/2026, 14:27:26
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        res = 0
        N = len(points)
        adj = {i: [] for i in range(N)} # {point: [distance, neighbor]} 
        for i in range(N):
            for j in range(i + 1, N):
                adj[i].append((distance(points[i], points[j]), j))
                adj[j].append((distance(points[i], points[j]), i))
        
        visited = set()
        minHeap = [[0, 0]] # start from first node, with no cost
        while len(visited) < N:
            cost, i = heapq.heappop(minHeap)
            if i not in visited:
                visited.add(i)
                res += cost
                for costNeigh, neigh in adj[i]:
                    if neigh not in visited:
                        heapq.heappush(minHeap, [costNeigh, neigh])
        
        return res

        

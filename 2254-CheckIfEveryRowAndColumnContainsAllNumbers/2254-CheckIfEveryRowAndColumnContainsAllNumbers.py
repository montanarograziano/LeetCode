# Last updated: 08/02/2026, 14:26:16
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        return all(set(r) == set([i for i in range(1, n + 1)]) for r in matrix) and all(set(c) == set([i for i in range(1, n + 1)]) for c in list(zip(*matrix)))
        
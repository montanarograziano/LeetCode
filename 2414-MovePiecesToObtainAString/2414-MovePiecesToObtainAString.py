# Last updated: 08/02/2026, 14:26:00
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        l, r = 0, 0
        n = len(start)
        while l < n or r < n:
            while l < n and start[l] == "_":
                l += 1
            while r < n and target[r] == "_":
                r += 1

            if l == n or r == n:
                break
            if start[l] != target[r] or start[l] == "L" and l < r or start[l] == "R" and l > r:
                return False
        
            l += 1
            r += 1
        return l == n and r == n

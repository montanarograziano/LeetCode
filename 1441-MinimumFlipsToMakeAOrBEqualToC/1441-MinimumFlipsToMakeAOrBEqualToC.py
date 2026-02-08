# Last updated: 08/02/2026, 14:27:56
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while a or b or c:
            x, y , z = a % 2, b % 2, c % 2
            if z == 0: 
                res += (x + y)
            elif x == 0 and y == 0:
                res += 1
            
            a >>= 1
            b >>= 1
            c >>= 1

        return res
                
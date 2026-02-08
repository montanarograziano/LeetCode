# Last updated: 08/02/2026, 14:28:16
class Solution:
    def tribonacci(self, n: int) -> int:
        first, second, third = 0, 1, 1
        if n == 0:
            return first
        if n < 3:
            return second
        for i in range(3, n + 1):
            new = first + second + third
            first = second
            second = third
            third = new
        return third
            

        
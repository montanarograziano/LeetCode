# Last updated: 08/02/2026, 14:25:37
class Solution:
    def countDigits(self, num: int) -> int:
        s = str(num)
        out = 0
        for n in s:
            if num % int(n) == 0:
                out += 1
        return out

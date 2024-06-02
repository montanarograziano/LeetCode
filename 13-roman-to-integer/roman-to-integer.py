class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        i = len(s) - 1
        while i >= 0:
            if i > 0 and d[s[i]] > d[s[i - 1]]:
                res += d[s[i]] - d[s[i - 1]]
                i -= 2
            else:
                res += d[s[i]]
                i -= 1
        return res

        
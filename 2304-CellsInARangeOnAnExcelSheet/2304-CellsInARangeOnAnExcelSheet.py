# Last updated: 08/02/2026, 14:26:11
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1, r1 = s.split(':')[0][0], int(s.split(':')[0][1])
        c2, r2 = s.split(':')[1][0], int(s.split(':')[1][1])
        c1_int, c2_int = ord(c1), ord(c2)
        l = []
        for i in range(c1_int, c2_int +1):
            for j in range(r1, r2 + 1):
                x = chr(i)
                y = str(j)
                l.append(x+y)
        return l


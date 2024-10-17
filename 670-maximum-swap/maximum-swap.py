class Solution:
    def maximumSwap(self, num: int) -> int:
        s = [c for c in str(num)]
        i = 0
        curmax = 0
        found = False
        id1, id2 = 0, 0
        while i < len(s) and not found:
            for j in range(len(s) - 1, i, -1):
                if int(s[j]) > int(s[i]) and int(s[j]) > curmax:
                    curmax = int(s[j])
                    id1, id2 = i, j
                    found = True
            i += 1
        s[id1], s[id2] = s[id2], s[id1]
        return int("".join(s))
        


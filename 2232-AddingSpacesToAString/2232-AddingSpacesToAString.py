# Last updated: 08/02/2026, 14:26:19
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        i, j = 0, 0
        while j < len(spaces):
            if i == spaces[j]:
                res.append(" ")
                res.append(s[i])
                j += 1
                i += 1
            else:
                res.append(s[i])
                i += 1
        if i < len(s):
            res.append(s[i:])
        return "".join(res) 
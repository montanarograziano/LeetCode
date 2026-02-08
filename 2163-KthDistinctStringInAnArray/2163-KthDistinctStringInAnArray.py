# Last updated: 08/02/2026, 14:26:52
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res = ""
        c = Counter(arr)
        i = 0
        for s, v in c.items():
            if v == 1:
                i += 1
                if i == k:
                    return s
        return res

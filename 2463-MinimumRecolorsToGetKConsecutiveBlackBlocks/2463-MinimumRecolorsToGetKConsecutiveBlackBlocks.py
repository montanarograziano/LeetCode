# Last updated: 08/02/2026, 14:25:56
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        j = k
        i = 0
        res = k + 1
        while j <= len(blocks):
            cur_blacks = blocks[i:j].count("B")
            res = min(res, k - cur_blacks)
            i += 1
            j += 1
        return res

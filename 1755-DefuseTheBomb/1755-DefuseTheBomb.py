# Last updated: 08/02/2026, 14:27:24
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)

        res = []
        n = len(code)
        if k > 0:
            for i, _ in enumerate(code):
                cur = 0
                for j in range(i + 1, i + k + 1):
                    cur += code[j % n]
                res.append(cur)
        else:
            for i, _ in enumerate(code):
                cur = 0
                for j in range(i + k, i):
                    cur += code[j % n]
                res.append(cur)

        return res

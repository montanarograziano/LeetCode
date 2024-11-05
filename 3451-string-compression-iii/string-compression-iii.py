class Solution:
    def compressedString(self, word: str) -> str:
        res = ""
        cur = ""
        for c in word:
            if len(cur) < 9 and (not cur or cur[-1] == c):
                cur += c
            elif cur[-1] != c:
                res += f"{len(cur)}{cur[-1]}"
                cur = c
            else:
                res += f"9{cur[-1]}"
                cur = c
        res = res + f"{len(cur)}{cur[-1]}" if cur else res
        return res

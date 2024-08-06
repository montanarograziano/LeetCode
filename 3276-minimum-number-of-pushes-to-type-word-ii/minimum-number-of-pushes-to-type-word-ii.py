class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        ordered = sorted(c.items(), key=lambda x: -x[1])
        res = 0
        for i, (w, n) in enumerate(ordered):
            res += n * (i // 8 + 1)
        return res
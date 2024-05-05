class Solution:
    def mostCommonWord(self, s: str, banned: List[str]) -> str:
        k = "!?',;."

        s = s.lower()
        for char in k:
            s = s.replace(char, ' ')

        co = Counter(s.split())

        mc = ""
        mf = 0

        for c, f in co.items():
            if c not in banned and f > mf:
                mc = c
                mf = f

        return mc

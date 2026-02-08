# Last updated: 08/02/2026, 14:27:22
from collections import Counter
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        d = Counter(allowed)
        l = 0
        consistent = True
        for w in words:
            consistent = True
            for c in w:
                if c not in d:
                    consistent = False
            if consistent:
                l += 1
        return l
                


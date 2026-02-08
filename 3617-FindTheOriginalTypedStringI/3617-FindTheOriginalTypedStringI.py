# Last updated: 08/02/2026, 14:24:56
class Solution:
    def possibleStringCount(self, word: str) -> int:
        n, ans = len(word), 1
        for i in range(1, n):
            if word[i - 1] == word[i]:
                ans += 1
        return ans
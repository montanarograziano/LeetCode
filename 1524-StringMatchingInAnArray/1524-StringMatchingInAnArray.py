# Last updated: 08/02/2026, 14:27:47
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res
# Last updated: 08/02/2026, 14:27:14
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        out = ""
        while i < len(word1) and i < len(word2):
            out += word1[i] + word2[i]
            i += 1
        
        if len(word1) >= i:
            out += word1[i:]

        if len(word2) >= i:
            out += word2[i:]
        
        return out

        
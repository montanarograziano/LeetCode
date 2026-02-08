# Last updated: 08/02/2026, 14:27:41
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        n = len(searchWord)
        for i, word in enumerate(words):
            if word[0:n] == searchWord:
                return i + 1
        return -1
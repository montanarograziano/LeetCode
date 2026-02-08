# Last updated: 08/02/2026, 14:25:41
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        for i, c in enumerate(sentence):
            if c == " ":
                if sentence[i - 1] != sentence[i + 1]:
                    return False
            if i == len(sentence) - 1:
                if sentence[i] != sentence[0]:
                    return False
        
        return True
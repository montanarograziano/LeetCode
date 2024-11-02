class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        l = sentence.split()
        l.append(l[0])
        for i in range(len(l) - 1):
            if l[i][-1] != l[i + 1][0]:
                return False
        return True
# Last updated: 08/02/2026, 14:25:55
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s) + 1)
        for left, right, d in shifts:
            prefix[right + 1] += 1 if d else -1
            prefix[left] += -1 if d else 1
        res = [ord(c) - ord('a') for c in s]
        diff = 0
        for i in reversed(range(len(prefix))):
            diff += prefix[i]
            res[i - 1] = (diff + res[i - 1]) % 26


        return "".join([chr(ord('a') + n) for n in res])

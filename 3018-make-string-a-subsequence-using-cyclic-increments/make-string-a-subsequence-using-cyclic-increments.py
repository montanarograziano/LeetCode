class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        l, r = 0, 0
        while l < len(str1) and r < len(str2):
            new = 'a' if str1[l] == 'z' else chr(ord(str1[l]) + 1)
            if str1[l] == str2[r] or new == str2[r]:
                l += 1
                r += 1
            else:
                l += 1
        return r == len(str2)
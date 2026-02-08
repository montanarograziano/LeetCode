# Last updated: 08/02/2026, 14:27:52
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = "aeiou"
        res = 0
        mask = 0
        mask_to_idx = {0: -1}
        for i, c in enumerate(s):
            if c in vowels:
                mask = mask ^ (1 + ord(c) - ord('a'))
            if mask in mask_to_idx:
                res = max(res, i - mask_to_idx[mask])
            else:
                mask_to_idx[mask] = i
            
        return res

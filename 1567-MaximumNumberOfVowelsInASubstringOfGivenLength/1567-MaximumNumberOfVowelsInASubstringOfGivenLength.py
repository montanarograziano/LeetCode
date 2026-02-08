# Last updated: 08/02/2026, 14:27:40
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cur = 0
        # Count vowels in first window
        for c in s[:k]:
            if c in 'aeiou':
                cur += 1
        out = cur
        prev = True if s[0] in 'aeiou' else False
        
        for i in range(1, len(s) - k + 1):
            if s[i + k - 1] in 'aeiou':
                cur += 1

            if s[i - 1] in 'aeiou':
                cur -= 1
            
            out = max(out, cur)
        
        return out
            
            

        

        
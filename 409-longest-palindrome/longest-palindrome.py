class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_count = 0
        n = len(s)
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        
        for k,v in d.items():
            if v % 2:
                odd_count += 1
            
        
        return n - odd_count + 1 if odd_count else n

        

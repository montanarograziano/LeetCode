class Solution:
    def isPalindrome(self, s: str, start: int, end: int) -> bool:
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        end = len(s)
        def dfs(i):
            if i >= end:
                res.append(part.copy())
            
            for j in range(i, end):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()
        
        dfs(0)
        return res
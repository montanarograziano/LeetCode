class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        cnt = 0
        last = ""
        for c in s:
            if c == last:
                cnt += 1           
            else:
                cnt = 0
            if cnt < 2:
                res += c
            last = c
        
        return res
            

        
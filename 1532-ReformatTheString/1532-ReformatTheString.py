# Last updated: 08/02/2026, 14:27:46
class Solution:
    def reformat(self, s: str) -> str:
        a, b = [], []
        for c in s:
            if c.isnumeric():
                a.append(c)
            else:
                b.append(c)
        
        if abs(len(a) - len(b)) > 1:
            return ""
        
        if len(a) < len(b): a,b = b, a
        
        out = ""
        while a:
            out += a.pop()
            if b:
                out += b.pop()
        
        return out


class Solution:
    def kthCharacter(self, k: int) -> str:
        l = 1
        s = "a"

        def next_s(s):
            out = ""
            for c in s:
                out += "a" if c == "z" else chr(ord(c) + 1)
            return out

        while l < k:
            cur = next_s(s)
            s += cur
            l += len(cur)
        
        return s[k - 1]
        
        
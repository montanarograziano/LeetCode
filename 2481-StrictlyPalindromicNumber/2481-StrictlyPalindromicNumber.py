# Last updated: 08/02/2026, 14:25:53
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:

        def toStr(n,base):
            convertString = "0123456789ABCDEF"
            if n < base:
                return convertString[n]
            else:
                return toStr(n//base,base) + convertString[n%base]


        def isPal(s: str) -> bool:
            i,j = 0, len(s) - 1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        for b in range(2, n - 1):
            if not isPal(toStr(n, b)):
                return False
        
        return True
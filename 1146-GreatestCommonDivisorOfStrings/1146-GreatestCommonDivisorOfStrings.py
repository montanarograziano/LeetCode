# Last updated: 08/02/2026, 14:28:21
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        out = ""
        i = 0
        def check_div(s, i):
            j = 1
            test = s[:i + 1] * j
            while len(test) <= len(s[i + 1:]):
                if test != s[i + 1:]:
                    j += 1
                    test = s[:i + 1] * j
                else:
                    return True
            return test == s[i + 1:] or s[i + 1:] == ""

        while i < len(str1) and i < len(str2) and str1[:i] == str2[:i]:
            # If they share a prefix, check if the remaining string is divisible
            if check_div(str1, i) and check_div(str2, i):
                out = str1[: i + 1]
            i += 1
        
        return out
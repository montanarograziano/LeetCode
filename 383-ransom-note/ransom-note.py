class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r, m = Counter(ransomNote), Counter(magazine)
        for k in r:
            if r[k] > m.get(k, 0):
                return False
        return True
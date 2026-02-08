# Last updated: 08/02/2026, 14:28:08
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:     
        c = Counter(arr)
        return len(set(c.values())) == len(c.values())
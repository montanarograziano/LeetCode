# Last updated: 08/02/2026, 14:26:10
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)
        return all(x % 2 == 0 for x in c.values())
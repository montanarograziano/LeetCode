class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)
        return all(x % 2 == 0 for x in c.values())
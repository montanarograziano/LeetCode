class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        res = [0, 0]
        for i, n in enumerate(nums):
            if target - n in d:
                return [d[target - n], i]
            d[n] = i
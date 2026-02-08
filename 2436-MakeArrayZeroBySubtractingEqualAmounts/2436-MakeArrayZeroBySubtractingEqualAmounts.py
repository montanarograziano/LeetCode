# Last updated: 08/02/2026, 14:25:56
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len({num for num in nums if num != 0})
        
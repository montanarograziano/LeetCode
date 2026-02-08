# Last updated: 08/02/2026, 14:26:09
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = set(nums[0])
        for n in nums[1:]:
            ans = ans & set(n)
        return sorted(ans)

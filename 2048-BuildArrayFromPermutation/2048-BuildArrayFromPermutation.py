# Last updated: 08/02/2026, 14:27:02
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i,n in enumerate(nums):
            ans.append(nums[nums[i]])
        return ans
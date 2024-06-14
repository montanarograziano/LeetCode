class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur_index = 0
        for i in [0, 1, 2]:
            cur_sum = 0
            for k in range(cur_index, len(nums)):
                if nums[k] == i:
                    cur_sum += 1
                    nums[cur_index], nums[k] = nums[k], nums[cur_index]
                    cur_index += 1
        return nums
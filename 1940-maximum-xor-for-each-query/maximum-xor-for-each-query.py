class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        prefix = [nums[0]] * n
        res = [0] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] ^ nums[i]
        
        max_xor = (2 ** maximumBit) - 1

        for i in range(n):
            res[i] = prefix[- i -1] ^ max_xor
        
        return res
        


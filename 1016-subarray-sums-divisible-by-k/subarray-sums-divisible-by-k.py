class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counts = Counter()
        counts[0] = 1
        running_sum = 0
        res = 0
        for num in nums:
            running_sum += num
            res += counts[running_sum % k]
            counts[running_sum % k] += 1
        return res
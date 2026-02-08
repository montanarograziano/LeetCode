# Last updated: 08/02/2026, 14:27:25
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        res = []
        c = sorted(Counter(nums).items(), key=lambda x: (x[1], -x[0]))
        for x in c:
            res.extend([x[0]] * x[1])
        return res
        
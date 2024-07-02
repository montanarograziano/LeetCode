class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        counter = Counter(nums1)
        for num in nums2:
            if num in counter and counter[num] > 0:
                counter[num] -= 1
                res.append(num)
        
        return res
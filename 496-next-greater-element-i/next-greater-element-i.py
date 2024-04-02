class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        mapping = {n: i for i,n in enumerate(nums2)}

        for j, n in enumerate(nums1):
            idx = mapping[n]
            for i in range(idx, len(nums2)):
                if nums2[i] > n:
                    ans[j] = nums2[i]
                    break
        
        return ans

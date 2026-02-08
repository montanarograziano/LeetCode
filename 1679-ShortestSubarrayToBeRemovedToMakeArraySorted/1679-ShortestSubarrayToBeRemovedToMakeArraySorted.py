# Last updated: 08/02/2026, 14:27:29
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        i = 0
        n = len(arr)
        r = n - 1
        while r > 0 and arr[r - 1] <= arr[r]:
            r -= 1
        
        res = r
        l = 0
        while l + 1 < n and arr[l] <= arr[l + 1]:
            l += 1
        
        res = min(res, n - 1 - l)

        l, r = 0, n - 1
        while l < r:
            while r < n and l + 1 < r and arr[r - 1] <= arr[r] and arr[l] <= arr[r]:
                r -= 1
            
            while r < n and arr[l] > arr[r]:
                r += 1
            
            res = min(res,  r - l - 1)
            if arr[l] > arr[l + 1]:
                break
            l += 1
        
        return res


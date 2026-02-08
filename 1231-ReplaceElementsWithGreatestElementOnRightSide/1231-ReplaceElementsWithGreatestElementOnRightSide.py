# Last updated: 08/02/2026, 14:28:17
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = arr[-1]
        i = len(arr) -2
        arr[-1] = -1
        if len(arr) == 1:
            return arr
        while i >= 0:
            temp = arr[i]
            arr[i] = m
            m = max(m, temp)
            i -= 1
        return arr

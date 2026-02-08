# Last updated: 08/02/2026, 14:27:28
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr)):
            cur = arr[i:i+m]
            if cur * k == arr[i:i+m*k]:
                return True

        return False


        
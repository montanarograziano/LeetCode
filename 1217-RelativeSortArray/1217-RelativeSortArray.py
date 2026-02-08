# Last updated: 08/02/2026, 14:28:17
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        counter = {num: 0 for num in arr2}
        remainer = []
        for num in arr1:
            if num not in counter:
                remainer.append(num)
            else:
                counter[num] += 1

        remainer.sort()
        for num in arr2:
            result.extend([num] * counter[num])
        
        result.extend(remainer)
        return result
        

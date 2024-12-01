class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = set()
        for i, n in enumerate(arr):
            if n % 2 == 0:
                if n / 2 in d:
                    return True
            if n * 2 in d:
                return True
            d.add(n)
        
        return False

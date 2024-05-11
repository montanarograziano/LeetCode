class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        def can_cover_all(radius):
            i, j = 0, 0
            while i < len(houses) and j < len(heaters):
                if abs(houses[i] - heaters[j]) <= radius:
                    i += 1
                else:
                    j += 1
            return i == len(houses)
        
        left, right = 0, max(houses[-1], heaters[-1])
        
        while left < right:
            mid = left + (right - left) // 2
            if can_cover_all(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
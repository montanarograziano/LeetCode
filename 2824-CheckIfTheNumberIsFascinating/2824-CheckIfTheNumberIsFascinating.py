# Last updated: 08/02/2026, 14:25:19
class Solution:
    def isFascinating(self, n: int) -> bool:
        if n > 333:
            return False
        
        if n % 10 == 5 or n % 10 == 0:
            return False
        
        num = str(n) + str(2 * n) + str(3 * n)
        
        return len(set(num)) == len(num) and '0' not in num
# Last updated: 08/02/2026, 14:26:17
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num%10==0 and num!=0:
            return False
        return True
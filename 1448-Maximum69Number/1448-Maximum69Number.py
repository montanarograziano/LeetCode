# Last updated: 08/02/2026, 14:27:54
class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))

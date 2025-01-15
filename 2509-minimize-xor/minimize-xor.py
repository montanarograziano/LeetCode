class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        a, b = num1.bit_count(), num2.bit_count()
        if a >= b:
            for _ in range(a - b):
                num1 = num1 & (num1 - 1)
        else:
            for _ in range(b - a):
                num1 = num1 | (num1 + 1)
        return num1
        
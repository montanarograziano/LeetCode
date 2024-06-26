class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(1 if s in set(jewels) else 0 for s in stones)
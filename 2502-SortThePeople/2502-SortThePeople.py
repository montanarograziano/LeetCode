# Last updated: 08/02/2026, 14:25:49
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [x[1] for x in sorted(list(zip(heights, names)), key=lambda x: x[0], reverse=True)]
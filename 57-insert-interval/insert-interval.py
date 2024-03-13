class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        res = []
        for i, interval in enumerate(intervals):
            # new is before the current interval
            if new[1] < interval[0]:
                res.append(new)
                return res + intervals[i:]
            # New is after the current one
            elif new[0] > interval[1]:
                res.append(interval)
            # Overlap
            else:
                new = [min(new[0], interval[0]), max(new[1], interval[1])]
            
        res.append(new)
        return res

        
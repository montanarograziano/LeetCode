class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        n = len(events)
        suffix = [0] * n
        suffix[n - 1] = events[n - 1][2]
        for i in range(n - 2, -1, -1):
            suffix[i] = max(events[i][2], suffix[i + 1])
        
        res = 0
        for i in range(n):
            left, right = i + 1, n - 1
            next_idx = -1
            while left <= right:
                mid = left + (right - left) // 2
                if events[mid][0] > events[i][1]:
                    next_idx = mid
                    right = mid - 1
                else:
                    left = mid + 1
            if next_idx != -1:
                res = max(res, events[i][2] + suffix[next_idx]) 
        res = max(max((x[2] for x in events)), res)  
        return res

# Last updated: 08/02/2026, 14:25:02
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        free_days = 0
        latest_end = 0
        for start, end in meetings:
            if start > latest_end:
                free_days += start - latest_end
            latest_end = max(latest_end, end + 1)
        free_days += days - latest_end
        return free_days

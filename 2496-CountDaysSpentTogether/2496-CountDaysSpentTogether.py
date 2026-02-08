# Last updated: 08/02/2026, 14:25:50
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        dom = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        m_start, d_start = list(map(int, arriveAlice.split('-')))
        alice_arrive_day = sum(dom[i] for i in range(m_start - 1)) + d_start
        m_end, d_end = list(map(int, leaveAlice.split('-')))
        alice_end_day = sum(dom[i] for i in range(m_end - 1)) + d_end

        m_start, d_start = list(map(int, arriveBob.split('-')))
        Bob_arrive_day = sum(dom[i] for i in range(m_start - 1)) + d_start
        m_end, d_end = list(map(int, leaveBob.split('-')))
        Bob_end_day = sum(dom[i] for i in range(m_end - 1)) + d_end

        range_days = max(0, min(Bob_end_day, alice_end_day) - max(Bob_arrive_day, alice_arrive_day) + 1)

        return range_days





        






        
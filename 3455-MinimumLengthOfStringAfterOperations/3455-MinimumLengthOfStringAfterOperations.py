# Last updated: 08/02/2026, 14:24:58
class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)
        delete_cnt = 0
        for k,v in c.items():
                if v % 2:
                    delete_cnt += v - 1
                else:
                    delete_cnt += v - 2
        return len(s) - delete_cnt



        
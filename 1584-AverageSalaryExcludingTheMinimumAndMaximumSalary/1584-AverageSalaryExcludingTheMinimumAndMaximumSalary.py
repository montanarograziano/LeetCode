# Last updated: 08/02/2026, 14:27:36
class Solution:
    def average(self, salary: List[int]) -> float:
        min = max = salary[0]
        sum = 0
        for i in salary:
            if i < min:
                min = i
            if i > max:
                max = i
            sum += i
        return (sum - min - max) / (len(salary) - 2)
        
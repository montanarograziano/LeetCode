# Last updated: 08/02/2026, 14:25:43
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        m, n = len(robot), len(factory)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m):
            dp[i][-1] = inf

        for j in range(n-1, -1, -1):
            distance_sum = 0
            min_distances = deque([(m, 0)])
            for i in range(m-1, -1, -1):
                distance_sum += abs(robot[i] - factory[j][0])
                # If the current robot is out of the limit of the current factory
                if min_distances[0][0] > i+factory[j][1]:
                    min_distances.popleft()
                # Remove the robots that are not in the limit of the current factory
                while min_distances and min_distances[-1][1] >= dp[i][j+1] - distance_sum:
                    min_distances.pop()
                min_distances.append((i, dp[i][j+1] - distance_sum))
                dp[i][j] = min_distances[0][1] + distance_sum

        return dp[0][0]
        
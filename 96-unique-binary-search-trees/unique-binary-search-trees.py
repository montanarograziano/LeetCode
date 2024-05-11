class Solution:
    def numTrees(self, n: int) -> int:
        dp = [-1] * (n + 1)
        
        def dfs(n, dp):
            if n <= 1:
                return 1
            
            if dp[n] != -1:
                return dp[n]
            
            res = 0
            for i in range(1, n + 1):
                res += dfs(i - 1, dp) * dfs(n - i, dp)
            
            dp[n] = res
            return dp[n]
        
        return dfs(n, dp)


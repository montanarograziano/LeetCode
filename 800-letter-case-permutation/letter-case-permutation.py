class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def dfs(i, subset):
            if i == len(s):
                res.append("".join(subset))
                return

            if s[i].isdigit():
                subset.append(s[i])
                dfs(i + 1, subset[:])
            else:
                # Swap
                subset.append(s[i].swapcase())
                dfs(i + 1, subset[:])
                subset.pop()
                # Not swap
                subset.append(s[i])
                dfs(i + 1, subset[:])

        
        dfs(0, [])
        return res
        
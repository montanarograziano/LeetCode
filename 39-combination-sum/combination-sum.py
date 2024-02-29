class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def backtrack(i):
            s = sum(subset)
            if s > target or i >= len(candidates):
                return
            if s == target:
                    res.append(subset[:])
                    return
            
            subset.append(candidates[i])
            backtrack(i)
            subset.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return res

        
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vow = 'aeiou'
        n = len(words)
        res = [0] * len(queries)
        prefix = [0] * n
        for i in range(n):
            if i == 0:
                prefix[0] = 1 if words[i][0] in vow and words[i][-1] in vow else 0
            else:
                prefix[i] = prefix[i - 1] + 1 if words[i][0] in vow and words[i][-1] in vow else prefix[i - 1]
        # print(prefix)      
        for i, (l,r) in enumerate(queries):
            left = 0 if l == 0 else prefix[l - 1]
            # print(prefix[r], left)
            res[i] = prefix[r] - left
        return res
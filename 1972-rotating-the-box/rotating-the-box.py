class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        N, M = len(box), len(box[0])
        res = [["."] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if box[i][j] == '*':
                    res[i][j] = '*'

        for r, row in enumerate(box):
            stones = row.count("#")
            obst_idx = row.index('*') if '*' in row else M
            i = M - 1
            while stones and i >= 0:
                if box[r][i] == ".":
                    j = i - 1
                    while j >= 0:
                        if box[r][j] == '#':
                            box[r][i] = '#'
                            box[r][j] = '.'
                            break
                        elif box[r][j] == '*':
                            break
                        else:
                            j -= 1
                i -= 1
        return list(zip(*box[::-1]))
                    
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        N, M = len(box), len(box[0])
        for r in range(N):
            i = M - 1
            for c in reversed(range(M)):
                if box[r][c] == '#':
                    box[r][i], box[r][c] = box[r][c], box[r][i]
                    i -= 1
                elif box[r][c] == '*':
                    i = c - 1
            
        return list(zip(*box[::-1]))
                    
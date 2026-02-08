# Last updated: 08/02/2026, 14:27:30
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        i,j = 0,len(mat[0])-1
        
        for row in mat:
            if len(row) > 1:
                
                if i == j :
                    res += row[i]
                else:
                    res += row[i]+row[j]

                i += 1
                j -= 1
            else:
                return row[0]
        return res
        
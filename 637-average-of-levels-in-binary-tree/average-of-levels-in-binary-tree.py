# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = deque()
        q.append(root)
        while q:
            s = 0
            c = 0
            for _ in range(len(q)):
                node = q.popleft()
                s += node.val
                c += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(s / c)
        
        return res


        
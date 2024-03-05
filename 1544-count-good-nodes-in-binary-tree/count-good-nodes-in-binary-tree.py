# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    good = 0
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, m):
            if not root:
                return
            
            m = max(m, root.val)
            if root.val >= m:
                self.good += 1
            
            if root.left:
                dfs(root.left, m)
            if root.right:
                dfs(root.right, m)
        

        dfs(root, root.val)
        return self.good

                
        
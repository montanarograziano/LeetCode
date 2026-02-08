# Last updated: 08/02/2026, 14:25:59
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root.left and not root.right:
                return root.val
            
            l = dfs(root.left)
            r = dfs(root.right)
            
            if root.val == 2:
                return l or r
            else:
                return l and r
        
        return dfs(root)
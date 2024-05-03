# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(root):
            if not root:
                return

            self.res += 1
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            return
        
        dfs(root)
        return self.res


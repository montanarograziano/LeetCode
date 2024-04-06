# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(root):
            if not root:
                return 0
            
            leftsum = max(0 , dfs(root.left))
            rightsum = max(0, dfs(root.right))
            self.res = max(root.val + leftsum + rightsum, self.res)

            return root.val + max(leftsum, rightsum)
        
        dfs(root)
        return self.res

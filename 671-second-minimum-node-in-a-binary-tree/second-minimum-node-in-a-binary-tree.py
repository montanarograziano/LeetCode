# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    m1, m2 = float("inf"), float("inf")
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root:
                return
            
            if root.val < self.m1:
                self.m1 = root.val
            elif root.val < self.m2 and root.val != self.m1:
                self.m2 = root.val
            
            if root.left:
                dfs(root.left)
            
            if root.right:
                dfs(root.right)
        
        dfs(root)
        return self.m2 if self.m2 != float("inf") else -1
        

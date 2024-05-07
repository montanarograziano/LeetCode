# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(root, cur):
            cur_sum = cur * 2 + root.val
            if not root.left and not root.right:
                self.res += cur_sum
            
            if root.left:
                dfs(root.left, cur_sum)
            if root.right:
                dfs(root.right, cur_sum)
        
        dfs(root, 0)
        return self.res
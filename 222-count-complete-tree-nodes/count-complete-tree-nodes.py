# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def count_left(root):
            height = 0
            while root:
                height += 1
                root = root.left
            return height

        def count_right(root):
            height = 0
            while root:
                height += 1
                root = root.right
            return height
        
            
        l = count_left(root)
        r = count_right(root)
        if l == r:
            return 2 ** l - 1
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

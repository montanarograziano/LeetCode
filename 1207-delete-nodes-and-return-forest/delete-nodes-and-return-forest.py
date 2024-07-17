# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        res = []
        if root.val not in to_delete:
            res.append(root)
        def dfs(root, parent):
            if not root:
                return        
            
            if root.left:
                dfs(root.left, root)
            if root.right:
                dfs(root.right, root)

            if root.val in to_delete:
                if root.left:
                    res.append(root.left)
                    root.left = None
                if root.right:
                    res.append(root.right)
                    root.right = None
                if parent and parent.left == root:
                    parent.left = None
                if parent and parent.right == root:
                    parent.right = None
        
        dfs(root, None)
        return res
            
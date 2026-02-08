# Last updated: 08/02/2026, 14:25:32
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def sumnodes(root, level=1):
            if not root:
                return
            
            if level == 1:
                root.val = 0
                if root.left:
                    root.left.val = 0
                if root.right:
                    root.right.val = 0
            else:
                l = root.left.val if root.left else 0
                r = root.right.val if root.right else 0
                if root.left:
                    root.left.val = sums[level + 1] - (l + r)
                if root.right:    
                    root.right.val = sums[level + 1] - (l + r)
            
            sumnodes(root.left, level + 1)
            sumnodes(root.right, level + 1)           
        
        q = deque([root])
        i = 0
        sums = {}
        while q:
            s = 0
            i += 1
            for _ in range(len(q)):
                cur = q.popleft()
                s += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            sums[i] = s
        
        sumnodes(root)
        return root
        

            


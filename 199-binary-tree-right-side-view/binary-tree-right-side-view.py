# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []
        
        q = deque()
        q.append(root)
        while q:
            found = False
            for _ in range(len(q)):
                cur = q.popleft()
                if not found:
                    res.append(cur.val)
                    found = True
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
        
        return res

        
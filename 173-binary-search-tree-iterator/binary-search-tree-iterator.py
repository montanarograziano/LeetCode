# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.array = []
        cur = root
        def inorder(root):
            if not root:
                return
            if root.left:
                inorder(root.left)
            self.array.append(root.val)
            if root.right:
                inorder(root.right)
        
        inorder(root)
        self.p = 0
        self.n = len(self.array)

        

    def next(self) -> int:
        self.p += 1
        return self.array[self.p - 1]
        

    def hasNext(self) -> bool:
        return 0 <= self.p < self.n
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
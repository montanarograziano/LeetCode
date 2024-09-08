# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n, ptr = 0, head
        n = 0
        while ptr:
            ptr = ptr.next
            n += 1
        
        dim, rem = n // k, n % k
        res = []
        ptr = head
        for _ in range(k):
            res.append(ptr)
            for _ in range(dim -1 + (1 if rem else 0)):
                if not ptr:
                    break
                ptr = ptr.next
            
            rem -= (1 if rem else 0)
            if ptr:
                ptr.next, ptr = None, ptr.next
        
        return res





# Last updated: 08/02/2026, 14:25:16
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        while ptr and ptr.next:
            tmp = ptr.next
            ptr.next = ListNode(math.gcd(ptr.val, ptr.next.val), tmp)
            ptr = tmp
        
        return head




        
# Last updated: 08/02/2026, 14:27:58
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        nums = []
        ptr = head
        out = 0
        while ptr:
            nums.append(str(ptr.val))
            ptr = ptr.next
        return int("".join(nums),2)
        


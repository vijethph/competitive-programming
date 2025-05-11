# https://leetcode.com/problems/reverse-linked-list-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # reach node at position "left"
        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next
        
        # now cur = "left", leftPrev = "node before left"
        # reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext
        
        # update pointers
        leftPrev.next.next = cur    # cur is node after "right"
        leftPrev.next = prev        # prev is "right"
        return dummy.next
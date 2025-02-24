# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # copy all elements to array and find if it is palindrome
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] != nums[right]:
                return False
            left += 1
            right -= 1
        
        return True

        # alternative optimized solution
        fast, slow = head, head

        # find middle (slow pointer)
        while fast and fast.next:
            fast = fast.next
            fast = fast.next
            slow = slow.next

        # reverse second hald
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
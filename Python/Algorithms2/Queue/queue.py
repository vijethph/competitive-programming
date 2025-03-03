# first in, first out queue
# 2 operations: enqueue (O(1)) and dequeue (O(1))
# easiest way to implement a queue is using linked lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self):
        self.left = None
        self.right = None

    def enqueue(self, val):
        new_node = ListNode(val)

        if self.right: # queue is not empty
            self.right.next = new_node
            self.right = self.right.next
        else: # queue is empty
            self.left = self.right = new_node

    def dequeue(self):
        if not self.left: # queue is empty
            return None

        # remove left node and return value
        res = self.left.val
        self.left = self.left.next
        if not self.left:
            self.right = None
        return res


        


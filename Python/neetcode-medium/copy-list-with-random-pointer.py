# https://leetcode.com/problems/copy-list-with-random-pointer/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = { None: None } # hashmap for all old and new nodes

        cur = head

        # first iteration - just create the nodes and assign them in hashmap
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        # second iteration
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        
        return oldToCopy[head]

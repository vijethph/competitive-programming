# stacks can be implemented using doubly linked lists
# leetcode problem: https://leetcode.com/problems/design-linked-list/description/

class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail # dummy node
        self.tail.prev = self.head # dummy node

    def get(self, index: int) -> int:
        """
        int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
        """
        curr = self.head.next # skip dummy node
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.tail and index == 0:
            return curr.val
        return -1
    
    def add_at_head(self, val: int) -> None:
        """
        void add_at_head(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = ListNode(val)
        curr, former = self.head.next, self.head
        former.next = new_node
        curr.prev = new_node
        new_node.next = curr
        new_node.prev = former
    
    def add_at_tail(self, val: int) -> None:
        """
        void add_at_tail(int val) Append a node of value val as the last element of the linked list.
        """
        new_node = ListNode(val)
        curr, former = self.tail, self.tail.prev
        former.next = new_node
        curr.prev = new_node
        new_node.next = curr
        new_node.prev = former

    def add_at_index(self, index: int, val: int) -> None:
        """
        void add_at_index(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
        """
        curr = self.head.next # skip dummy node
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            new_node = ListNode(val)
            former = curr.prev
            former.next = new_node
            curr.prev = new_node
            new_node.next = curr
            new_node.prev = former
    
    def delete_at_index(self, index: int) -> None:
        """
        void delete_at_index(int index) Delete the indexth node in the linked list, if the index is valid.
        """
        curr = self.head.next # skip dummy node
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.tail and index == 0:
            latter, former = curr.next, curr.prev
            latter.prev = former
            former.next = latter
        
    

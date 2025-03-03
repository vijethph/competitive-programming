# double ended queue / deque

class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        # create 2 dummy nodes and link them
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def is_empty(self) -> bool:
        return self.head.next == self.tail
    
    def append(self, value) -> None:
        new_node = ListNode(value)
        last_node = self.tail.prev

        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node
    
    def append_left(self, value) -> None:
        new_node = ListNode(value)
        first_node = self.head.next

        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first_node
        first_node.prev = new_node
    
    def pop(self) -> int:
        if self.is_empty():
            return -1

        last_node = self.tail.prev
        value = last_node.value
        prev_node = last_node.prev

        prev_node.next = self.tail
        self.tail.prev = prev_node
        return value
    
    def pop_left(self) -> int:
        if self.is_empty():
            return -1
        
        first_node = self.head.next
        value = first_node.value 
        next_node = first_node.next

        self.head.next = next_node
        next_node.prev = self.head
        return value

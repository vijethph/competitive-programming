# linked lists can be in random order in memory, but they are connected via pointers
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        # Init the list with a 'dummy' node which makes 
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        """
        int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
        """
        count = 0
        curr = self.head.next # first node
        while curr:
            if count == index:
                return curr.val
            curr = curr.next
            count += 1
        return -1
            

    def insert_head(self, val: int) -> None:
        """
        void insert_head(int val) will insert a node with val at the head of the list.
        """
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node # pointer of dummy node to the new node
        if not new_node.next:
            self.tail = new_node # if list was empty before insertion

    def insert_tail(self, val: int) -> None:
        """
        void insert_tail(int val) will insert a node with val at the tail of the list.
        """
        new_node = ListNode(val)
        self.tail.next = new_node # update old tail
        self.tail = new_node # change the tail

    def remove(self, index: int) -> bool:
        """
        bool remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true
        """
        count = 0
        curr = self.head # dummy node
        
        while count < index and curr:
            curr = curr.next
            count += 1
        
        if curr and curr.next:
            if curr.next == self.tail: # if it is the end of list
                self.tail = curr
            curr = curr.next.next # curr.next is the one to be removed
            return True
        return False


    def get_values(self) -> List[int]:
        """
        int[] get_values() return an array of all the values in the linked list, ordered from head to tail.
        """
        curr = self.head.next
        res = []
        
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res


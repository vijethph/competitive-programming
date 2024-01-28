
class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self):
        return f"{self.data}"

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __str__(self):
        return "->".join([str(item) for item in self])

    def __len__(self):
        return sum(1 for _ in self)

    def insert_at_head(self, data):
        self.insert_at_nth(0, data)

    def insert_at_tail(self, data):
        self.insert_at_nth(len(self), data)

    def insert_at_nth(self, index, data):
        length = len(self)

        if not 0 <= index <= length:
            raise ValueError("Invalid index")

        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        elif index == 0:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        elif index == length:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.previous.next = new_node
            new_node.previous = temp.previous
            new_node.next = temp
            temp.previous = new_node

    def delete_head(self):
        self.delete_at_nth(0)

    def delete_tail(self):
        self.delete_at_nth(len(self) - 1)

    def delete_at_nth(self, index: int):
        length = len(self)

        if not 0 <= index < length - 1:
            raise ValueError("Invalid index")

        delete_node = self.head
        if length == 1:
            self.head = self.tail = None
        elif index == 0:
            self.head = self.head.next
            self.head.previous = None
        elif index == length - 1:
            delete_node = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            delete_node = temp
            temp.next.previous = temp.previous
            temp.previous.next = temp.next

        return delete_node.data

    def delete(self, data) -> str:
        current = self.head

        while current.data !=data:
            if current.next:
                current = current.next
            else:
                raise ValueError("Data not in list")

        if current == self.head:
            self.delete_head()
        elif current == self.tail:
            self.delete_tail()
        else:
            current.previous.next = current.next
            current.next.previous = current.previous
        return data

    def is_empty(self):
        return len(self) == 0

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_head(1)
    dll.insert_at_head(2)
    dll.insert_at_head(3)
    dll.insert_at_head(4)
    dll.insert_at_head(5)
    dll.insert_at_head(6)
    dll.insert_at_head(7)
    dll.insert_at_head(8)
    dll.insert_at_head(9)
    dll.insert_at_head(10)
    print(dll)
    dll.delete_head()
    print(dll)
    dll.delete_tail()
    print(dll)
    dll.delete_at_nth(3)
    print(dll)
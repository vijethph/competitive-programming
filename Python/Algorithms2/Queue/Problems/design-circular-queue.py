# https://leetcode.com/problems/design-circular-queue/description/

class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyCircularQueue:
    def __init__(self, k: int):
        self.front = None
        self.rear = None
        self.max_size = k
        self.curr_size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        newNode = Node(value)
        if self.isEmpty():
            self.front = newNode
        else:
            self.rear.next = newNode
        self.rear = newNode
        self.rear.next = self.front
        self.curr_size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.curr_size == 1:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        self.curr_size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.val

    def isEmpty(self) -> bool:
        return self.curr_size == 0

    def isFull(self) -> bool:
        return self.curr_size == self.max_size
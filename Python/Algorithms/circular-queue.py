class CircularQueue:
    def __init__(self, n: int):
        self.n = n
        self.array = [None] * self.n
        self.front = 0
        self.rear = 0
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def first(self):
        return False if self.is_empty() else self.array[self.front]

    def enqueue(self, data):
        if self.size >= self.n:
            raise Exception("Queue is full")
        self.array[self.rear] = data
        self.rear = (self.rear + 1) % self.n
        self.size += 1
        return self

    def dequeue(self):
        if self.size == 0:
            raise Exception("Queue is empty")
        temp = self.array[self.front]
        self.array[self.front] = None
        self.front = (self.front + 1) % self.n
        self.size -= 1
        return temp

from __future__ import annotations

from collections.abc import Iterator
from typing import Any

class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Node | None = None

    def __str__(self) -> str:
        return f"{self.data}"

class LinkedQueue:
    def __init__(self) -> None:
        self.front: Node | None = None
        self.rear: Node | None = None

    def __iter__(self) -> Iterator[Any]:
        node = self.front
        while node:
            yield node.data
            node = node.next

    def __len__(self) -> int:
        return len(tuple(iter(self)))

    def __str__(self) -> str:
        return "<-".join([str(item) for item in self])

    def is_empty(self) -> bool:
        return len(self) == 0

    def put(self, item: Any) -> None:
        node = Node(item)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            assert isinstance(self.rear, Node)
            self.rear.next = node
            self.rear = node

    def get(self) -> Any:
        if self.is_empty():
            raise Exception("Queue is empty")

        assert isinstance(self.front, Node)
        node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return node.data

    def clear(self) -> None:
        self.front = None
        self.rear = None

if __name__ == "__main__":
    queue = LinkedQueue()
    print(queue)
    queue.put("first")
    queue.put("second")
    queue.put("third")
    print(queue)
    print(queue.get())

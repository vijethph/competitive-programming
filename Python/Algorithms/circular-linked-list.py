from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    """Class Node"""

    data: Any
    next_node: Node | None = None


@dataclass
class CircularLinkedList:
    head: Node | None = None
    tail: Node | None = None

    def __iter__(self) -> Iterator:
        node = self.head
        while node:
            yield node.data
            node = node.next_node
            if node == self.head:
                break

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def __repr__(self) -> str:
        return "->".join([str(item) for item in self])

    def insert_tail(self, data: Any) -> None:
        """Inserts an element at the end of the list"""
        self.insert_nth(len(self), data)

    def insert_head(self, data: Any) -> None:
        """Inserts an element at the beginning of the list"""
        self.insert_nth(0, data)

    def insert_nth(self, index: int, data: Any) -> None:
        """Inserts an element at the nth position"""
        if index < 0 or index > len(self):
            raise ValueError("Invalid index")
        new_node: Node = Node(data)
        if self.head is None:
            new_node.next_node = self.head
            self.head = self.tail = new_node
        elif index == 0:
            new_node.next_node = self.head
            assert self.tail is not None
            self.head = self.tail.next_node = new_node
        else:
            temp: Node | None = self.head
            for _ in range(index - 1):
                assert temp is not None
                temp = temp.next_node
            assert temp is not None
            assert temp.next_node is not None
            delete_node = temp.next_node
            temp.next_node = temp.next_node.next_node
            if index == len(self) - 1:
                self.tail = temp
        return delete_node.data

    def is_empty(self) -> bool:
        """Returns True if the list is empty"""
        return len(self) == 0


if __name__ == "__main__":
    cll = CircularLinkedList()
    assert cll.is_empty() is True
    cll.insert_nth(0, 1)
    assert cll.is_empty() is False
    cll.insert_tail(2)
    assert cll.tail.data == 2
    cll.insert_head(0)
    assert cll.head.data == 0
    assert cll.tail.data == 2

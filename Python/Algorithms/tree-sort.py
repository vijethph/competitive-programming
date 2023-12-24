from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Node:
    val: int
    left: Node | None = None
    right: Node | None = None

    def __iter__(self) -> Iterator[int]:
        if self.left:
            yield from self.left
        yield self.val
        if self.right:
            yield from self.right

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def insert(self, val: int) -> None:
        if val < self.val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)


def tree_sort(arr: list[int]) -> tuple[int, ...]:
    if len(arr) == 0:
        return tuple(arr)
    root = Node(arr[0])
    for item in arr[1:]:
        root.insert(item)
    return tuple(root)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item.strip()) for item in user_input.split(",")]
    print(tree_sort(unsorted))

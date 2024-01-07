from __future__ import annotations

from collections.abc import Iterator, Iterable
from dataclasses import dataclass
from typing import Any, Self
from pprint import pformat


@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None
    parent: Node | None = None

    def __iter__(self) -> Iterator[int]:
        yield from self.left or []
        yield self.value
        yield from self.right or []

    def __repr__(self) -> str:
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({f"{self.value}": (self.left, self.right)}, indent=1)

    @property
    def is_right(self) -> bool:
        return bool(self.parent and self is self.parent.right)


@dataclass
class BinarySearchTree:
    root: Node | None = None

    def __bool__(self) -> bool:
        return bool(self.root)

    def __iter__(self) -> Iterator[int]:
        yield from self.root or []

    def __str__(self) -> str:
        return str(self.root)

    def __reassign_nodes(self, node: Node, new_children: Node | None) -> None:
        if new_children is not None:
            new_children.parent = node.parent
        if node.parent is not None:
            if node.is_right:
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def empty(self) -> bool:
        return not self.root

    def __insert(self, value: int) -> None:
        new_node = Node(value)
        if self.empty():
            self.root = new_node
        else:
            parent_node = self.root
            if parent_node is None:
                return
            while True:
                if value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node = parent_node.left
                else:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
            new_node.parent = parent_node

    def insert(self, *values: int) -> None:
        for value in values:
            self.__insert(value)
        return self

    def search(self, value) -> Node | None:
        if self.empty():
            raise IndexError("Empty tree")
        else:
            node = self.root
            while node is not None and node.value is not value:
                node = node.left if value < node.value else node.right
            return node

    def get_max(self, node: Node | None = None) -> Node | None:
        if node is None:
            if self.root is None:
                return None
            node = self.root

        if not self.empty():
            while node.right is not None:
                node = node.right
        return node

    def get_min(self, node: Node | None = None) -> Node | None:
        if node is None:
            if self.root is None:
                return None
            node = self.root

        if not self.empty():
            node = self.root
            while node.left is not None:
                node = node.left
        return node

    def remove(self, value: int) -> None:
        node = self.search(value)
        if node is None:
            msg = f"Node with value {value} not found in tree"
            raise ValueError(msg)

        if node.left is None and node.right is None:
            self.__reassign_nodes(node, None)
        elif node.left is None:
            self.__reassign_nodes(node, node.right)
        elif node.right is None:
            self.__reassign_nodes(node, node.left)
        else:
            predecessor = self.get_max(node.left)
            self.remove(predecessor.value)
            node.value = predecessor.value

    def preorder_traverse(self, node: Node | None = None) -> Iterable[int]:
        if node is not None:
            yield node
            yield from self.preorder_traverse(node.left)
            yield from self.preorder_traverse(node.right)

    def traversal_tree(self, traversal_function=None) -> Any:
        if traversal_function is None:
            return self.preorder_traverse(self.root)
        else:
            return traversal_function(self.root)

    def inorder(self, arr: list, node: Node | None) -> None:
        if node:
            self.inorder(arr, node.left)
            arr.append(node.value)
            self.inorder(arr, node.right)

    def find_kth_smallest(self, k: int, node: Node) -> int:
        arr: list[int] = []
        self.inorder(arr, node)
        return arr[k - 1]


def inorder(curr_node: Node | None) -> list[Node]:
    node_list = []
    if curr_node is not None:
        node_list = inorder(curr_node.left) + [curr_node] + inorder(curr_node.right)
    return node_list


def postorder(curr_node: Node | None) -> list[Node]:
    node_list = []
    if curr_node is not None:
        node_list = postorder(curr_node.left) + postorder(curr_node.right) + [curr_node]
    return node_list


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(8, 3, 6, 1, 10, 14, 13, 4, 7)
    print(bst)
    print(bst.search(6))
    print(bst.get_max())
    print(bst.get_min())
    print(bst.remove(3))
    print(bst)
    print(bst.traversal_tree(inorder))
    print(bst.traversal_tree(postorder))
    print(bst.find_kth_smallest(3, bst.root))

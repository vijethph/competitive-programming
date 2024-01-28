from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class StackOverflowError(BaseException):
    pass


class StackUnderflowError(BaseException):
    pass


class Stack(Generic[T]):
    def __init__(self, limit: int = 10):
        self.stack = list[T] = []
        self.limit = limit

    def __bool__(self) -> bool:
        return bool(self.stack)

    def __str__(self) -> str:
        return str(self.stack)

    def push(self, data: T) -> None:
        if len(self.stack) >= self.limit:
            raise StackOverflowError("Stack Overflow")
        self.stack.append(data)

    def pop(self) -> T:
        if not self.stack:
            raise StackUnderflowError
        return self.stack.pop()

    def peek(self) -> T:
        if not self.stack:
            raise StackUnderflowError
        return self.stack[-1]

    def is_empty(self) -> bool:
        return not bool(self.stack)

    def is_full(self) -> bool:
        return self.size() == self.limit

    def size(self) -> int:
        return len(self.stack)

    def __contains__(self, item: T) -> bool:
        return item in self.stack


if __name__ == "__main__":
    stack = Stack()
    for i in range(10):
        stack.push(i)
    print(stack)
    print(stack.is_full())
    print(stack.pop())
    print(stack.peek())
    print(stack.is_empty())
    print(stack.size())
    print(5 in stack)
    print(10 in stack)

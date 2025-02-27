# all of them are O(1) operations, implemented using dynamic arrays in respective programming languages

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
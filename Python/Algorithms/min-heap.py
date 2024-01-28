class Node:
    def __init__(self, name, val):
        self.name = name
        self.val = val

    def __str__(self):
        return f"{self.__class__.__name__}({self.name}, {self.val})"

    def __lt__(self, other):
        return self.val < other.val


class MinHeap:
    def __init__(self, array):
        self.idx_of_element = {}
        self.heap_dict = {}
        self.heap = self.build_heap(array)

    def __getitem__(self, key):
        return self.heap_dict[key]

    def get_parent_idx(self, idx):
        return (idx - 1) // 2

    def get_left_child_idx(self, idx):
        return idx * 2 + 1

    def get_right_child_idx(self, idx):
        return idx * 2 + 2

    def get_value(self, idx):
        return self.heap[idx].val

    def build_heap(self, array):
        last_idx = len(array) - 1
        start_from = self.get_parent_idx(last_idx)

        for idx, i in enumerate(array):
            self.idx_of_element[i] = idx
            self.heap_dict[i.name] = i.val

        for i in range(start_from, -1, -1):
            self.sift_down(i, array)
        return array

    def sift_down(self, idx, array):
        while True:
            left_child_idx = self.get_left_child_idx(idx)
            right_child_idx = self.get_right_child_idx(idx)

            smallest = idx
            if left_child_idx < len(array) and array[left_child_idx] < array[idx]:
                smallest = left_child_idx
            if right_child_idx < len(array) and array[right_child_idx] < array[smallest]:
                smallest = right_child_idx

            if smallest != idx:
                array[idx], array[smallest] = array[smallest], array[idx]
                (
                    self.idx_of_element[array[idx]],
                    self.idx_of_element[array[smallest]],
                ) = (
                    self.idx_of_element[array[smallest]],
                    self.idx_of_element[array[idx]],
                )
                idx = smallest
            else:
                break

    def sift_up(self, idx, array):
        p = self.get_parent_idx(idx)
        while p >= 0 and self.heap[p] > self.heap[idx]:
            self.heap[p], self.heap[idx] = self.heap[idx], self.heap[p]
            (
                self.idx_of_element[self.heap[p]],
                self.idx_of_element[self.heap[idx]],
            ) = (
                self.idx_of_element[self.heap[idx]],
                self.idx_of_element[self.heap[p]],
            )
            idx = p
            p = self.get_parent_idx(idx)

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.idx_of_element[self.heap[0]], self.idx_of_element[self.heap[-1]] = (
            self.idx_of_element[self.heap[-1]],
            self.idx_of_element[self.heap[0]],
        )

        x = self.heap.pop()
        del self.idx_of_element[x]
        self.sift_down(0, self.heap)
        return x

    def insert(self, node):
        self.heap.append(node)
        self.idx_of_element[node] = len(self.heap) - 1
        self.heap_dict[node.name] = node.val
        self.sift_up(len(self.heap) - 1, self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def decrease_key(self, node, new_value):
        assert self.heap[self.idx_of_element[node]].val > new_value
        node.val = new_value
        self.heap_dict[node.name] = new_value
        self.sift_up(self.idx_of_element[node], self.heap)


r = Node("R", -1)
b = Node("B", 6)
a = Node("A", 3)
x = Node("X", 1)
e = Node("E", 4)
my_min_heap = MinHeap([r, b, a, x, e])

print("Min Heap - before decrease key")
for i in my_min_heap.heap:
    print(i)

print("Min Heap - After decrease key of node [B -> -17]")
my_min_heap.decrease_key(b, -17)

for i in my_min_heap.heap:
    print(i)

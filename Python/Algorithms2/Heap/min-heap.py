# priority queue is an abstract data type (an interface definition) 
# that defines three operations: is_empty, insert_with_priority, and pull_highest_priority_element. 
# The definition says what those functions are expected to do, but it doesn't say how it is to be implemented

# A binary heap is one way to implement a priority queue. 
# Its advantages are ease of implementation and that it is reasonably efficient. 
# Whereas a heap is definitely a priority queue, by no means is it true that a priority queue is a heap.
# A binary heap is a complete binary tree. For a min heap, a node's children should always be greater than the node. Duplicate nodes are allowed
# They are implemented using arrays, skipping the first index

# Easy way to find nodes:
# leftChild = 2 * idx
# rightChild = 2 * idx + 1
# parent = idx / 2


class MinHeap:
    def __init__(self):
        self.heap = [0]
    
    def push(self, val): # O(log n)
        # push new value at the end and percolate it up to maintain order
        self.heap.append(val)
        idx = len(self.heap) - 1

        # percolate up
        while self.heap[idx] < self.heap[i // 2]:
            tmp = self.heap[idx]
            self.heap[idx] = self.heap[i // 2]
            self.heap[i // 2] = tmp # swap with parent
            idx = idx // 2
    
    def pop(self): # O(log n)
        # remove root, put the last node in the root and percolate it down to maintain order
        if len(self.heap) == 1:
            return None
        elif len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        idx = 1

        # percolate down
        while 2 * idx < len(self.heap):
            # if right exists and right < left and newcur > right
            if (2 * idx + 1 < len(self.heap) and self.heap[2 * idx + 1] < self.heap[2 * idx] and self.heap[idx] > self.heap[2 * idx + 1]):
                # swap right child
                tmp = self.heap[i]
                self.heap[idx] = self.heap[2 * idx + 1]
                self.heap[2 * idx + 1] = tmp
                idx = 2 * idx + 1
            elif self.heap[idx] > self.heap[2 * idx]:
                # swap left child
                tmp = self.heap[idx]
                self.heap[idx] = self.heap[2 * idx]
                self.heap[2 * idx] = tmp
                idx = 2 * idx
            else:
                break
        
        return res

    # heapify takes a random list of elements and puts it into a heap in O(n) time
    def heapify(self, arr):
        # 0th position is moved to the end
        arr.append(arr[0])

        self.heap = arr
        cur = (len(self.heap) - 1) // 2 # skip all leaf nodes

        while cur > 0:
            # percolate down
            idx = cur
            while 2 * idx < len(self.heap):
                # if right exists and right < left and newcur > right
                if (2 * idx + 1 < len(self.heap) and self.heap[2 * idx + 1] < self.heap[2 * idx] and self.heap[idx] > self.heap[2 * idx + 1]):
                    # swap right child
                    tmp = self.heap[i]
                    self.heap[idx] = self.heap[2 * idx + 1]
                    self.heap[2 * idx + 1] = tmp
                    idx = 2 * idx + 1
                elif self.heap[idx] > self.heap[2 * idx]:
                    # swap left child
                    tmp = self.heap[idx]
                    self.heap[idx] = self.heap[2 * idx]
                    self.heap[2 * idx] = tmp
                    idx = 2 * idx
                else:
                    break
            cur -= 1
        
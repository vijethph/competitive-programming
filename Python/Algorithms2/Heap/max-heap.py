class MaxHeap:
    def __init__(self):
        self.heap = [0]
    
    def push(self, val): # O(log n)
        # push new value at the end and percolate it up to maintain order
        self.heap.append(val)
        idx = len(self.heap) - 1

        # percolate up
        while idx > 1 and self.heap[idx] > self.heap[idx // 2]:
            # swap with parent
            self.heap[idx], self.heap[idx // 2] = self.heap[idx // 2], self.heap[idx]
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
            # find the larger child index
            large_idx = 2 * idx
            if (2 * idx + 1 < len(self.heap) and self.heap[2 * idx + 1] > self.heap[2 * idx]):
                large_idx = 2 * idx + 1
            
            # if the current node is larger than the larger child, no operations required
            if self.heap[idx] >= self.heap[large_idx]:
                break
            
            # swap with the larger child
            self.heap[idx], self.heap[large_idx] = self.heap[large_idx], self.heap[idx]
            idx = large_idx
        
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
                # find the larger child
                large_idx = 2 * idx
                if (2 * idx + 1 < len(self.heap) and self.heap[2 * idx + 1] > self.heap[2 * idx]):
                    large_idx = 2 * idx + 1
                
                # if the current node is larger than the larger child, no operations required
                if self.heap[idx] >= self.heap[large_idx]:
                    break
                
                # swap with the larger child
                self.heap[idx], self.heap[large_idx] = self.heap[large_idx], self.heap[idx]
                idx = large_idx
            cur -= 1
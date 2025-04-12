# https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # BFS with min heap / priority queue
        # time: O(E * log V)
        edges = collections.defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))
        
        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue   
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        
        return t if len(visit) == n else -1
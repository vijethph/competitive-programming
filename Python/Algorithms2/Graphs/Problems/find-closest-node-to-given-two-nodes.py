# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adj = collections.defaultdict(list)
        for i, dst in enumerate(edges):
            adj[i].append(dst)
        
        def bfs(src, distmap):
            q = deque()
            q.append([src, 0])
            distmap[src] = 0

            while q:
                node, dist = q.popleft()
                for nei in adj[node]:
                    if nei not in distmap:
                        q.append([nei, dist + 1])
                        distmap[nei] = dist + 1

        

        node1dist = {} # map node -> distance from node1
        node2dist = {} # map node -> distance from node2
        bfs(node1, node1dist)
        bfs(node2, node2dist)

        res = -1
        resdist = float("inf")

        for i in range(len(edges)):
            if i in node1dist and i in node2dist:
                dist = max(node1dist[i], node2dist[i])
                if dist < resdist:
                    res = i
                    resdist = dist
        
        return res
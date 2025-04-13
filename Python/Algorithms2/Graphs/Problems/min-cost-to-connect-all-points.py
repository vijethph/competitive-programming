# https://leetcode.com/problems/min-cost-to-connect-all-points/description/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # minimum spanning tree - prim's algorithm - O(n^2 log n)
        n = len(points)
        graph = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                graph[i][j] = graph[j][i] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                edges.append((graph[i][j], i, j))
        edges.sort()
        parent = list(range(n))
        rank = [0] * n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1
            return True
        cost = 0
        for w, u, v in edges:
            if union(u, v):
                cost += w
        return cost
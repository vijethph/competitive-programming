# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # start at city 0 and recursively check its neighbours
        # count outgoing edges

        edges = { (a,b) for a,b in connections }
        neighbors = { city:[] for city in range(n) }
        visit = set()
        changes = 0

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        def dfs(city):
            nonlocal edges, neighbors, visit, changes
            
            for neighbor in neighbors[city]:
                if neighbor in visit:
                    continue
                
                if (neighbor, city) not in edges:
                    changes += 1

                visit.add(neighbor)
                dfs(neighbor)
            
        visit.add(0)
        dfs(0)
        return changes

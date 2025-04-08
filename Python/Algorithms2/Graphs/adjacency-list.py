# nodes = vertices
# pointers connecting nodes = edges
# (number of edges) e <= v^2 (number of vertices), where every node can have a maximum of v edges (including an edge to itself)

# trees and linked lists are directed graphs

# graphs are represented using matrix, adjacency matrix and adjacency lists

# matrix - 2d array, where there can be undirected edge from elements having 0, and 1 represents block
# adjacency - dimensions represents the number of nodes, where 1 represents a directed edge from row node to col node
# adjacency list - similar to linked lists, where each node has a value and a list of neighbor nodes (edges from that node)

# GraphNode used for adjacency list
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

# or use a HashMap
adjList = { "A": [], "B": [] }

# given directed edges, build an adjacency list
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

adjList = {}

for src, dst in edges:
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []
    adjList[src].append(dst)

# count paths (backtracking)
# time: O(N^v) where N is the number of connected nodes, and v is the height of the tree
def dfs(node, target, adjList, visit):
    if node in visit:
        return 0
    if node == target:
        return 1

    count = 0
    visit.add(node)

    for neighbor in adjList[node]:
        count += dfs(neighbor, target, adjList, visit)
    visit.remove(node)

    return count

# example
print(dfs("A", "E", adjList, set()))

# shortest path from node to target
# time: O(v + e) where v is the number of nodes and e is the number of edges
# space: O(v) where e is the number of nodes
def bfs(node, target, adjList):
    length = 0
    visit = set()
    visit.add(node)
    queue = deque()
    queue.append(node)

    while queue:
        for i in range(len(queue)):
            curr = queue.popleft()
            if curr == target:
                return length
            
            for neighbor in adjList[curr]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)
        
        length += 1
    
    return length

# example
print(bfs("A", "E", adjList))
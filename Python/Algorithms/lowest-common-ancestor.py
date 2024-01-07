from __future__ import annotations
from queue import Queue


def swap(a: int, b: int) -> tuple[int, int]:
    a ^= b
    b ^= a
    a ^= b
    return a, b


def create_sparse(max_node: int, parent: list[list[int]]) -> list[list[int]]:
    j = 1
    while (1 << j) < max_node:
        for i in range(1, max_node + 1):
            parent[j][i] = parent[j - 1][parent[j - 1][i]]
        j += 1
    return parent


def lowest_common_ancestor(u: int, v: int, level: list[int], parent: list[list[int]]) -> int:
    if level[u] < level[v]:
        u, v = swap(u, v)
    for i in range(18, -1, -1):
        if level[u] - (1 << i) >= level[v]:
            u = parent[i][u]

    if u == v:
        return u
    for i in range(18, -1, -1):
        if parent[i][u] not in [0, parent[i][v]]:
            u, v = parent[i][u], parent[i][v]
    return parent[0][u]


def breadth_first_search(
    level: list[int], parent: list[list[int]], max_node: int, graph: dict[int, list[int]], root: int = 1
) -> tuple[list[int], list[list[int]]]:
    level[root] = 0
    q: Queue[int] = Queue(maxsize=max_node)
    q.put(root)
    while q.qsize() > 0:
        u = q.get()
        for v in graph[u]:
            if level[v] == -1:
                level[v] = level[u] + 1
                parent[0][v] = u
                q.put(v)
        return level, parent


def main() -> None:
    max_node = 13
    parent = [[0 for _ in range(max_node + 10)] for _ in range(20)]
    level = [-1 for _ in range(max_node + 10)]
    graph: dict[int, list[int]] = {
        1: [2, 3, 4],
        2: [5],
        3: [6, 7],
        4: [8],
        5: [9, 10],
        6: [11],
        7: [],
        8: [12, 13],
        9: [],
        10: [],
        11: [],
        12: [],
        13: [],
    }
    level, parent = breadth_first_search(level, parent, max_node, graph, 1)
    parent = create_sparse(max_node, parent)
    print(lowest_common_ancestor(11, 12, level, parent))


if __name__ == "__main__":
    main()

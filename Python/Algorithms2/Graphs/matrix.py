# matrix dfs
# count the unique paths from the top left to the bottom right
# a single path may only move along 0's and can't visit the same cell more than once
# count paths (backtracking)
# time: O(4 ^(n * m)), where n - number of rows, m - number of cols
# space: O(n * m)
def dfs(grid, row, col, visit):
    ROWS, COLS = len(grid), len(grid[0])
    if (min(row, col) < 0               # if element pointer goes out of bounds
        or row == ROWS or col == COLS   # if element pointer goes out of bounds
        or (row, col) in visit          # if already visited - visit is a hashset
        or grid[row][col] == 1):        # if there is a block
        return 0
    if row == ROWS - 1 or col == COLS - 1: # we found the path
        return 1
    
    visit.add(row, col)

    count = 0
    count += dfs(grid, row + 1, col, visit)
    count += dfs(grid, row - 1, col, visit)
    count += dfs(grid, row, col + 1, visit)
    count += dfs(grid, row, col - 1, visit)

    visit.remove((row, col))
    return count

# example
print(dfs(grid, 0, 0, set()))

# shortest path from top left to bottom right
# time: O(n * m), where n - number of rows, m - number of cols
# space: O(n * m)
def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque()
    queue.append((0, 0))
    visit.add((0, 0))

    length = 0
    while queue:
        for i in range(len(queue)):
            row, col = queue.popleft()
            if row == ROWS - 1 and col == COLS - 1:
                return length
            
            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]] # directions
            for dr, dc in neighbors:
                if (min(row + dr, col + dc) < 0             # if element pointer goes out of bounds
                    or row + dr == ROWS or col + dc == COLS # if element pointer goes out of bounds
                    or (row + dr, col + dc) in visit        # if already visited - visit is a hashset
                    or grid[row + dr][col + dc] == 1):      # if there is a block
                    continue

                queue.append((row + dr, col + dc))
                visit.add((row + dr, col + dc))
        
        length += 1

# example
print(bfs(grid))

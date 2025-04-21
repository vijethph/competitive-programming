# If the result of the subproblem depends on two variables, this is where 2-dimensional dynamic programming comes into picture

# memoization / top down dynamic programming - time and space: O(n * m)
def memoization(row, col, ROWS, COLS, cache):
    if row == ROWS or col == COLS:
        return 0
    if cache[row][col] > 0:
        return cache[row][col]
    if row == ROWS - 1 or col == COLS - 1:
        return 1
    
    cache[row][col] = (memoization(row + 1, col, ROWS, COLS, cache) + memoization(row, col + 1, ROWS, COLS, cache))
    return cache[row][col]

# print(memoization(0, 0, 4, 4, [[0] * 4 for i in range(4)]))

# bottom up dynamic programming -  time: O(n * m), space: O(m), where m is the number of columns
def dp(ROWS, COLS):
    prevRow = [0] * COLS

    for row in range(ROWS - 1, -1, -1):
        curRow = [0] * COLS
        curRow[COLS - 1] = 1
        for col in range(COLS - 2, -1, -1):
            curRow[col] = curRow[col + 1] + prevRow[col]
        prevRow = curRow
    
    return prevRow[0]

# print(dp(4, 4))
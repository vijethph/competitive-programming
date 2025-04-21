# 1 dimensional dynamic programming
# It is basically an optimized version of recursion. it tackles a big problem by breaking down into smaller subproblems, usually more time and space efficient.
# Memoization is an optimization technique which stores computation results in cache, and retrieves that same information from the cache the next time it's needed instead of computing it again

# Memoization / Top Down dynamic programming
def memoization(n, cache):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    
    cache[n] = memoization(n - 1) + memoization(n - 2)
    return cache[n]

# print(memoization(5, {}))

# Bottom Up dynamic programming
def dp(n):
    if n < 2:
        return n
    
    dp = [0, 1]
    i = 2
    while i <= n:
        tmp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = tmp
        i += 1
    return dp[1]

# print(dp(10))
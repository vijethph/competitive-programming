# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        # recurrence relation: rob = max(arr[0] + arr[2:n], rob[1:n])
        # max of (rob 1st house + remaining ones skipping adjacent, rob 2nd house and remaining ones)
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2 
            rob2 = temp 
        return rob2
# https://leetcode.com/problems/all-possible-full-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {0 : [], 1: [TreeNode()] } # map n: list of full binary trees

        # return the list of full binary trees with n nodes:
        def backtrack(n):
            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]
            if n in dp:
                return dp[n]
            
            res = []
            for left in range(n):
                right = n - 1 - left
                leftTrees, rightTrees = backtrack(left), backtrack(right)

                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0, t1, t2))
            
            dp[n] = res
            return res
        
        return backtrack(n)
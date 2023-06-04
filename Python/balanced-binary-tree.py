# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def dfs(node):
            if node is None:
                return 0

            nonlocal ans
            l = dfs(node.left)
            r = dfs(node.right)
            # When the difference between two sub-trees is more than 1
            if abs(l - r) > 1: ans = False

            return max(l, r) + 1

        dfs(root)
        return ans
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderIdx = {v:i for i, v in enumerate(inorder)}

        def helper(left, right):
            if left >  right:
                return None
            
            root = TreeNode(postorder.pop())

            idx = inorderIdx[root.val]
            root.right = helper(idx + 1, right)
            root.left = helper(left, idx - 1)
            return root
        
        return helper(0, len(inorder) - 1)
# https://leetcode.com/problems/binary-tree-right-side-view/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        que = collections.deque([root])

        while que:
            rs = None

            for i in range(len(que)):
                node = que.popleft()
                if node:
                    rs = node
                    que.append(node.left)
                    que.append(node.right)
            
            if rs:
                res.append(rs.val)
            
        return res

        

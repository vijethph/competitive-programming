# time: O(n) as all nodes are visited
# space: O(h) where h is the height of the tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    # all these three traversals are depth-first search
    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)
    
    def preorder(self, root):
        if not root:
            return

        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
        
    def postorder(self, root):
        if not root:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val)
        
# binary trees are always guaranteed to have leaf nodes
# cycles are not allowed in binary trees
# a binary tree is a connected, undirected graph with no cycles

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# for any target, binary search tree essentially divides nodes into 2 similar to binary search algorithm
# search is O(logn) only if the binary search tree is balanced (heights differ only by 1 for any sub-tree)
# inserting and deleting nodes is O(logn) as well
# to remove a node with 2 children - pick the smallest value in right subtree, or the largest value in left subtree of the node
    def find_min_value_node(self, root):
        cur = root

        while cur and cur.left:
            cur = cur.left
        return cur
    
    def find_max_value_node(self, root):
        cur = root

        while cur and cur.right:
            cur = cur.right
        return cur

    def insert(self, root, val):
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insert(root.right, val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        return root

    def remove(self, root, val):
        if not root:
            return None

        if val > root.val:
            root.right = self.remove(root.right, val)
        elif val < root.val:
            root.left = self.remove(root.left, val)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_node = self.find_min_value_node(root.right)
                root.val = min_node.val
                root.right = remove(root.right, min_node.val)

        return root

    def search(self, root, target):
        if not root:
            return None
        
        if target > root.val:
            return self.search(root.right, target)
        elif target < root.val:
            return self.search(root.left, target)
        else:
            return root
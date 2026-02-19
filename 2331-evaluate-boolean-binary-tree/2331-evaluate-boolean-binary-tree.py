class Solution(object):
    def evaluateTree(self, root):
        
        # Leaf node
        if not root.left and not root.right:
            return bool(root.val)
        
        # Evaluate left & right
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        
        # OR operation
        if root.val == 2:
            return left or right
        
        # AND operation
        if root.val == 3:
            return left and right

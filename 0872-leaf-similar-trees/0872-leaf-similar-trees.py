# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1=[]
        leaf2=[]
        def leaf(root,l):
            if not root:
                return
            if root.left is None and root.right is None:
                l.append(root.val)
            leaf(root.left,l)
            leaf(root.right,l)
        leaf(root1,leaf1)
        leaf(root2,leaf2)
        return leaf1==leaf2
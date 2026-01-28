# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        l=[]
        def values(root,l):
            if not root:
                return
            values(root.left,l)
            l.append(root.val)
            values(root.right,l)
        values(root,l)
        l=sorted(l)
        mn=float('inf')
        for i in range(1,len(l)):
            mn=min(mn,l[i]-l[i-1])
        return mn
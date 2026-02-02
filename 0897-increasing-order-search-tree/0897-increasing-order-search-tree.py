# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        val=[]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            val.append(root.val)
            dfs(root.right)
        dfs(root)
        new=TreeNode(val[0])
        x=new
        for i in range(1,len(val)): 
            n=TreeNode(val[i])
            x.right=n
            x=n
        return new

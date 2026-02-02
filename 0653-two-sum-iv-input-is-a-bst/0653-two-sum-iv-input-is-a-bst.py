# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        val=[]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            val.append(root.val)
            dfs(root.right)
        dfs(root)
        for i in range(len(val)):
            for j in range(i+1,len(val)):
                if val[i]+val[j]==k:
                    return True
        return False
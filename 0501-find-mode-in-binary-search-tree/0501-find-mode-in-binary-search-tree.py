# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            l.append(root.val)
            dfs(root.right)
        dfs(root)
        c=Counter(l)
        mx=max(c.values())
        ans=[]
        for i in c:
            if c[i]==mx:
                ans.append(i)
        return ans
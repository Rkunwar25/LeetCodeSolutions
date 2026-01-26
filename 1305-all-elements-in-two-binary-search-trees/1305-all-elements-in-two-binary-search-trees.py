# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        tree1=[]        
        tree2=[]
        def dfs(root,ans):
            if not root:
                return 
            dfs(root.left,ans)
            ans.append(root.val)
            dfs(root.right,ans)
        dfs(root1,tree1)
        dfs(root2,tree2)
        tree1.extend(tree2)
        return sorted(tree1)
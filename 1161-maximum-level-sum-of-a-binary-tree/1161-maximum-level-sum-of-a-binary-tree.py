# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def level(root):
            if not root:
                return []
            result=[]
            q=deque([root])
            while q:
                level=[]
                size=len(q)
                for _ in range(size):
                    node=q.popleft()
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                result.append(level)         
            return result
        ans=level(root)
        mx=float('-inf')
        level=0
        for i in ans:
            if sum(i)>mx:
                mx=sum(i)
                level=ans.index(i)+1
        return level
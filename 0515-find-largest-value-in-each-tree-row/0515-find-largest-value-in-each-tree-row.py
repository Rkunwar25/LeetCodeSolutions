# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
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
        sol=[]
        for i in ans:
            sol.append(max(i))
        return sol
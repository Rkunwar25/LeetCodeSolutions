class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return
            res.append(node.val)          # Root
            for child in node.children:  # Children
                dfs(child)

        dfs(root)
        return res

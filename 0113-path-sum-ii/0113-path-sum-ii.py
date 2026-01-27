class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, curr_sum, path):
            if not node:
                return

            curr_sum += node.val
            path.append(node.val)

            # Check if it's a leaf and sum matches
            if not node.left and not node.right and curr_sum == targetSum:
                res.append(path[:])  # copy path

            dfs(node.left, curr_sum, path)
            dfs(node.right, curr_sum, path)

            path.pop()  # backtrack

        dfs(root, 0, [])
        return res

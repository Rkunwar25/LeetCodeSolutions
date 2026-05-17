class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n

        def dfs(i):
            # Out of bounds or already visited
            if i < 0 or i >= n or visited[i]:
                return False

            # Found a zero
            if arr[i] == 0:
                return True

            visited[i] = True

            # Try both possible jumps
            return dfs(i + arr[i]) or dfs(i - arr[i])

        return dfs(start)
class Solution:
    def kWeakestRows(self, mat, k):
        arr = []

        # Count soldiers in each row and store (count, index)
        for i in range(len(mat)):
            soldiers = sum(mat[i])
            arr.append((soldiers, i))

        # Sort by soldier count, then by row index
        arr.sort()

        # Extract first k row indices
        ans = []
        for i in range(k):
            ans.append(arr[i][1])

        return ans
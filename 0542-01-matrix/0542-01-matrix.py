from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        dist = [[float('inf')] * n for _ in range(m)]
        queue = deque()

        # Step 1: Initialize queue with all 0s
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))

        # Step 2: BFS from all 0s
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            i, j = queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if dist[ni][nj] > dist[i][j] + 1:
                        dist[ni][nj] = dist[i][j] + 1
                        queue.append((ni, nj))

        return dist

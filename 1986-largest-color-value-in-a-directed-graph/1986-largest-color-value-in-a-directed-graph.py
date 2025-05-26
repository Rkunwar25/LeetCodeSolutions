from collections import defaultdict, deque

class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        color_count = [[0] * 26 for _ in range(n)]
        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        visited = 0
        max_color_value = 0

        while queue:
            node = queue.popleft()
            visited += 1
            color_index = ord(colors[node]) - ord('a')
            color_count[node][color_index] += 1
            max_color_value = max(max_color_value, color_count[node][color_index])

            for neighbor in graph[node]:
                for c in range(26):
                    color_count[neighbor][c] = max(color_count[neighbor][c], color_count[node][c])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if visited < n:
            return -1

        return max_color_value

from collections import deque


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.adjacency_matrix = [[0] * n for _ in range(n)]
        for src, dst in edges:
            self.adjacency_matrix[src][dst] = 1
            self.adjacency_matrix[dst][src] = 1

        visited_levels = {}
        def bfs(src):
            q = deque()
            q.append(src)
            visited_levels[src] = 0
            level = 0
            while q:
                v = q.popleft()
                level += 1
                parent_count = 1

                for i in range(n):
                    if self.adjacency_matrix[v][i] == 1:
                        if i in visited_levels and parent_count == 0:
                            return False

                        elif visited_levels[v] > visited_levels.get(i, level):
                            parent_count -= 1

                        if i not in visited_levels:
                            visited_levels[i] = level
                            q.append(i)

                        # Check for sibling connections
                        if visited_levels[v] == visited_levels[i]:
                            return False
            return True
            
        res= bfs(0)
        for i in range(1,n):
            if i not in visited_levels:
                return False
        return res

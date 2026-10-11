class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific = {(0, j) for j in range(n)}
        atlantic = {(m - 1, j) for j in range(n)}
        for i in range(m):
            pacific.add((i, 0))
            atlantic.add((i, n - 1))

        # get source nodes:
        def get_src_neighbors(node):
            res = []
            i, j = node
            if 0 <= i - 1 < m and heights[i][j] <= heights[i - 1][j]:
                res.append((i - 1, j))

            if 0 <= i + 1 < m and heights[i][j] <= heights[i + 1][j]:
                res.append((i + 1, j))

            if 0 <= j - 1 < n and heights[i][j] <= heights[i][j - 1]:
                res.append((i, j - 1))

            if 0 <= j + 1 < n and heights[i][j] <= heights[i][j + 1]:
                res.append((i, j + 1))

            return res

        atlantic_sources = set()
        pacific_sources = set()

        def populate_sources(src, sources_set):
            stk = [src]
            visited = {src}
            while stk:
                v = stk.pop()
                sources_set.add(v)
                for src_node in get_src_neighbors(v):
                    if src_node not in visited:
                        stk.append(src_node)
                        visited.add(src_node)

        for node in pacific:
            populate_sources(node,pacific_sources)

        for node in atlantic:
            populate_sources(node,atlantic_sources)
        
        return [list(t) for t in atlantic_sources.intersection(pacific_sources)]
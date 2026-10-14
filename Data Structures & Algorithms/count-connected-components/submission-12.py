class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.adjacency_list = {}
        unvisited = set(x for x in range(n))

        for src, dst in edges:
            l_s = self.adjacency_list.get(src, [])
            l_d = self.adjacency_list.get(dst, [])
            l_s.append(dst)
            l_d.append(src)
            self.adjacency_list[src] = l_s
            self.adjacency_list[dst] = l_d

        connections = 0

        def dfs(src):
            stk = [src]
            while stk:
                v = stk.pop()
                if v in unvisited:
                    unvisited.remove(v)

                for dst in self.adjacency_list.get(v, []):
                    if dst in unvisited:
                        stk.append(dst)

        while unvisited:
            src = unvisited.pop()
            connections += 1
            dfs(src)
        return connections

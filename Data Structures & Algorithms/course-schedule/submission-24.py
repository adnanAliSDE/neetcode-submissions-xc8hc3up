class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.adjacency_list = {}
        self.size = numCourses

        for course, pre in prerequisites:
            l = self.adjacency_list.get(course, [])
            l.append(pre)

            self.adjacency_list[course] = l

        visited = set()

        def dfs(course):
            if self.adjacency_list.get(course, []) == []:
                return True

            visited.add(course)
            for pre in self.adjacency_list[course]:
                if pre in visited or dfs(pre) == False:
                    return False
                else:
                    self.adjacency_list[course].remove(pre)

            visited.remove(course)

            return True

        for course in self.adjacency_list:
            if dfs(course) == False:
                return False
        return True

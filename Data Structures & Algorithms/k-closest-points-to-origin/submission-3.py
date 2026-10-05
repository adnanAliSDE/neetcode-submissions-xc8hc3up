class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        decorated = [(x * x + y * y, x, y) for i, (x, y) in enumerate(points)]
        heapq.heapify(decorated)

        res = []
        for _ in range(k):
            item = heapq.heappop(decorated)
            dist, x, y = item
            res.append([x, y])

        return res

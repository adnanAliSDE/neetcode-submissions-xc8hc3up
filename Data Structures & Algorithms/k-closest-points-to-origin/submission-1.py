import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = {}
        for idx, point in enumerate(points):
            x, y = point
            d = math.sqrt(x * x + y * y)
            d_arr = distances.get(d, [])
            d_arr.append(idx)
            distances[d] = d_arr

        res = []
        d_arr = list(distances.keys())
        heapq.heapify(d_arr)
        while k > 0:
            d_elem = heapq.heappop(d_arr)
            point_indices = distances[d_elem]
            iteration_count = min(k, len(point_indices))
            for i in range(iteration_count):
                res.append(points[point_indices[i]])
            k = k - iteration_count
        return res

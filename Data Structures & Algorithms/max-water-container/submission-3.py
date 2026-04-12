class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        start = 0
        end = n - 1

        max_area = 0
        while start < end:
            breadth = end - start

            if heights[start] < heights[end]:
                area = heights[start] * breadth
                start = start + 1
            else:
                area = heights[end] * breadth
                end = end - 1

            if area > max_area:
                max_area = area
        return max_area
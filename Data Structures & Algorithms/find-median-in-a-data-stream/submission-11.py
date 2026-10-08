import heapq


class MedianFinder:
    def __init__(self):
        self.test_input = [2, 4, 3, 1, 7, 8, 9, 3, 6, 4, 5]
        self.left_max_heap = []
        self.right_min_heap = []

    # Main logic
    def addNum(self, num: int) -> None:
        heapq.heappush(self.right_min_heap, num)
        # Since we need elements in ordered manner that's why we are adding in right and then moving it to left_max_heap
        if len(self.right_min_heap) - 1 > len(self.left_max_heap):
            right = heapq.heappop(self.right_min_heap)
            heapq.heappush(self.left_max_heap, -right)

        if (self.left_max_heap and self.right_min_heap) and self.right_min_heap[0] < (-self.left_max_heap[0]):
            left = -heapq.heappop(self.left_max_heap)
            right = heapq.heappop(self.right_min_heap)
            heapq.heappush(self.left_max_heap, -right)
            heapq.heappush(self.right_min_heap, left)

    @property
    def item_count(self):
        return len(self.left_max_heap) + len(self.right_min_heap)

    @property
    def both_empty(self):
        return self.left_max_heap == [] and self.right_min_heap == []

    def findMedian(self) -> float:

        if self.item_count == 0:
            return None

        if self.item_count % 2 == 0:
            left = -self.left_max_heap[0]
            right = self.right_min_heap[0]
            return (left + right) / 2
        else:
            return self.right_min_heap[0]

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap=[-x for x in nums]
        heapq.heapify(nums)
        self.k=k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,-val)
        return -1*heapq.nsmallest(self.k,self.heap)[-1]

        

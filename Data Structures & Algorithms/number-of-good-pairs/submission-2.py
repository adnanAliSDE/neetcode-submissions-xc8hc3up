from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=Counter(nums)
        return sum(k*(k-1)//2 for k in count.values())
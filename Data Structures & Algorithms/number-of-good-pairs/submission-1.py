class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        tr_count = {}
        good_count = 0
        for num in nums:
            num_count = tr_count.get(num, 0) + 1
            tr_count[num] = num_count

        for count in tr_count.values():
            if count>1:
                good_count+=count*(count-1)//2

        return good_count

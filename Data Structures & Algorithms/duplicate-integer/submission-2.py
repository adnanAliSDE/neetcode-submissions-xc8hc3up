class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for num in nums:
            num_count = counter.get(num, None)
            if num_count is not None:
                return True

            counter[num] = 1
        return False

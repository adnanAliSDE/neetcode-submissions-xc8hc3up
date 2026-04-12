class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        has_duplicate=False
        for i in range(n):
            for j in range(n):
                if nums[i]==nums[j] and i!=j:
                    has_duplicate=True
        return has_duplicate
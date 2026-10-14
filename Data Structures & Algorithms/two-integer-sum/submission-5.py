class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, num in enumerate(nums):
            if seen.get((target - num), None) is not None:
                return [seen[target - num], idx]
            seen[num] = idx

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, val in enumerate(nums):
            complement = target - val
            if seen.get(complement, -1) != -1:
                return [seen[complement], idx]
            else:
                seen[val] = idx
        return []
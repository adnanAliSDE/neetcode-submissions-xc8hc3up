class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        table = nums[:2]
        table.append(nums[2] + nums[0])
        for i in range(3, n):
            val = max(table[i - 2], table[i - 3])
            table.append(val + nums[i])
        return max(table)

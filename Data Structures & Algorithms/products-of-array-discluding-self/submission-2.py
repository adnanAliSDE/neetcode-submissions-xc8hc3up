class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1

        def calculate_suff(idx):
            res = 1
            if idx + 1 > len(nums):
                return res
            for i in range(idx + 1, len(nums)):
                res *= nums[i]
            return res

        for idx in range(len(nums)):
            suffix *= nums[idx]

        outputs = []
        for idx in range(len(nums)):
            suffix = suffix // nums[idx] if nums[idx] != 0 else calculate_suff(idx)
            product = prefix * suffix
            outputs.append(product)
            prefix *= nums[idx]
        return outputs

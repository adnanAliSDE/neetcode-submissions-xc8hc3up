class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        outputs=[1]*n
        prefix=1
        suffix=1

        for i in range(1,n):
            prefix=prefix*nums[i-1]
            outputs[i]=prefix*outputs[i]

        for i in range(n-2,-1,-1):
            suffix=suffix*nums[i+1]
            outputs[i]=suffix*outputs[i]
        
        return outputs
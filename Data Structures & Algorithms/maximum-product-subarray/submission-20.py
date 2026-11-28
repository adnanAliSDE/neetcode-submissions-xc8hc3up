class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=-float('inf')

        pre=1
        suff=1
        for i in range(len(nums)):
            pre=pre*nums[i]
            suff=suff*nums[len(nums)-1-i]

            ans=max(ans,pre,suff)
            
            if not pre:
                pre=1
            if not suff:
                suff=1
        return ans

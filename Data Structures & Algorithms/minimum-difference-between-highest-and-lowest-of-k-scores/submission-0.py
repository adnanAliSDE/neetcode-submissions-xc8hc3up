class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        r=k-1
        n=len(nums)
        if k>n:
            return
        diff=nums[r]-nums[l]
        res=diff

        while r<n-1:
            l+=1
            r+=1
            res=min(res,nums[r]-nums[l])
        return res
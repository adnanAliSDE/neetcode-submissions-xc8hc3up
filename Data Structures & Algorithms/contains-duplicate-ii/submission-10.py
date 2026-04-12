class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        r=k
        n=len(nums)

        if k<1 or n==1:
            return False
        s=set()
        for i in range(l,r+1):
            if nums[i] in s:
                return True
            s.add(nums[i])
        
        while r<n-1:
            s.remove(nums[l])
            l+=1
            r+=1
            if nums[r] in s:
                return True
            s.add(nums[r])
        return False

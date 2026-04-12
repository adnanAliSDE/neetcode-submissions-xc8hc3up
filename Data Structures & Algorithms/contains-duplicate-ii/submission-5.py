class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)

        l,r=0,k
        if k<1:
            return False

        i=0
        while True:
            if i==n-1:
                break
            s=set()
            for i in range(l,r+1):
                if nums[i] in s:
                    return True
                s.add(nums[i])
            l=l+1
            r=r+1

        return False

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        min_idx=(left+right)//2
        while left<=right:
            mid=(left+right)//2

            if nums[left]>=nums[mid]<=nums[right]:
                min_idx=mid if nums[mid]<nums[min_idx] else min_idx

            if nums[mid]>=nums[right]:
                left=mid+1
            else:
                right=mid-1
        
        def bSearch(arr,left,right,target):
            if left>right:
                return -1
            mid=(left+right)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]<target:
                left=mid+1
            else:
                right=mid-1
            
            return bSearch(arr,left,right,target)
        
        idx_s1=bSearch(nums,min_idx,len(nums)-1,target)
        if idx_s1==-1:
            return bSearch(nums,0,min_idx-1,target)
        else:
            return idx_s1


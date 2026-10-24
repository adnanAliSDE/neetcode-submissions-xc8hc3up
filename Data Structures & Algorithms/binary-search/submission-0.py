class Solution:
    def search(self, arr: List[int], target: int) -> int:
        left,right=0,len(arr)-1

        while left<=right:
            mid=(left+right)//2
            if target==arr[mid]: 
                return mid
            elif target>arr[mid]:
                left=mid+1
            
            elif target<arr[mid]:
                right=mid-1
        return -1
            

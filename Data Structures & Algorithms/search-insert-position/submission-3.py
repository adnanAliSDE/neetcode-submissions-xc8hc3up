class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
            left, right = 0, len(arr) - 1
            mid=(left+right)//2
            while left <= right:
                mid=(left+right)//2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            # if arr[mid]<target:
            #     return mid+1
            # else:
            return (left+right)//2+1

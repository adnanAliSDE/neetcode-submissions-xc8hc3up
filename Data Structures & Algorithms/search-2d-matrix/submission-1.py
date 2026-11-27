class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # Find the row
        row = None
        left, right = 0, m-1
        while left <= right:
            mid = (left + right) // 2
            a, b = matrix[mid][0], matrix[mid][-1]
            if a <= target <= b:
                row = matrix[mid]
                break
            elif target > b:
                left = mid + 1
            else:
                right = mid - 1

        if row is None:
            return False

        left,right=0,n-1
        while left<=right:
            mid=(left+right)//2
            if row[mid]==target:
                return True
            elif target>row[mid]:
                left=mid+1
            else:
                right=mid-1
        return False

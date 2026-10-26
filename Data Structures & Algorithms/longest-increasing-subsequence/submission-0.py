class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        table=[]
        for i in range(len(nums)):
            table.append(1)
            for j in range(i):
                if nums[j]<nums[i]:
                    table[-1]=max(table[j]+1,table[-1])
        
        return max(table)
                
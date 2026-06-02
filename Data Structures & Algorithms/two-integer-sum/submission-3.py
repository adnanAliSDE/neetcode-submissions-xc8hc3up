class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}

        for i in range(len(nums)):
            d[target-nums[i]]=i
        
        res=[]
        for j in range(len(nums)):
            i=d.get(nums[j],None)
            if i is not None and i!=j:
                return [j,i]

        
        
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts.sort()
        n=len(gifts)
        if n==0:
            return None
        for i in range(k):
            gifts[n-1]=floor(sqrt(gifts[n-1]))
            gifts.sort() 
        
        return sum(gifts)



        
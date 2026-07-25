import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        n=len(gifts)

        if n==0:
            return 0
        for _ in range(k):
            max_num=gifts[0]
            mi=0
            for idx in range(1,n):
                if gifts[idx]>max_num:
                    max_num=gifts[idx]
                    mi=idx
            gifts[mi]=math.isqrt(max_num)
    
        return sum(gifts)       
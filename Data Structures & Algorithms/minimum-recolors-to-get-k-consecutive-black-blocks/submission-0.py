class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        r=k-1
        n=len(blocks)
        if k>n:
            return

        ops=0
        for i in range(l,r+1):
            if blocks[i]=='W':
                ops+=1

        min_ops=ops
        while r<n-1:
            if blocks[l]=='W':
                ops=ops-1
            l+=1
            r+=1
            if blocks[r]=='W':
                ops+=1
            min_ops=min(ops,min_ops)
        return min_ops
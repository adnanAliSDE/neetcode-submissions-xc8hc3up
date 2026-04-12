from collections import Counter
class Solution:
    def isAnagram(self,s, t):
        # 1.
        # keys = set(s).union(set(t))
        # ds = dict((key, 0) for key in keys)
        # dt = dict((key, 0) for key in keys)

        # for i in s:
        #     ds[i] += 1

        # for j in t:
        #     dt[j] += 1

        # return ds == dt

        #2. 
        #  return Counter(s)==Counter(t)

        # 3. 
        ds ={}
        for i in s:
            ds[i]=ds.get(i,0)+1
        
        for i in t:
            ds[i]=ds.get(i,0)-1
            if ds[i]==0:
                del ds[i]
        
        return len(ds)==0
class Solution:
    def isAnagram(self,s, t):
        keys = set(s).union(set(t))
        ds = dict((key, 0) for key in keys)
        dt = dict((key, 0) for key in keys)

        for i in s:
            ds[i] += 1

        for j in t:
            dt[j] += 1

        return ds == dt
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        matched = 0
        curr = 0
        for char in t:
            if curr<n and s[curr] == char:
                matched += 1
                curr += 1
        if matched == n:
            return True
        else:
            return False

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        seen={}

        l=max_len=0
        for r in range(n):
            char=s[r]

            if char in seen and seen[char]>=l:
                max_len=max(max_len,r-l)
                l=seen[char]+1
            elif r==n-1:
                max_len=max(max_len,r-l+1)
            seen[char]=r
        return max_len
            
            
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        start = 0
        end = n - 1

        while start < end:
            while start < n and not s[start].isalnum():
                start = start + 1

            while end >= 0 and not s[end].isalnum():
                end = end - 1
            
            if start >=n or end<0:
                continue
            if s[start].lower() != s[end].lower():
                return False
            start = start + 1
            end = end - 1

        return True
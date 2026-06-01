class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if not s[i:] or s[i]!=strs[0][i]:
                    return prefix
            prefix+=strs[0][i]
        return prefix
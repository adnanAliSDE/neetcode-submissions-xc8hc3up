class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        if len(strs)==0:
            return prefix

        for i in range(len(strs[0])):
            for s in strs:
                if i>=len(s) or s[i]!=strs[0][i]:
                    return prefix
            prefix+=strs[0][i]
        return prefix
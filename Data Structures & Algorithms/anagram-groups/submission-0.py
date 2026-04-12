from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        anagrams = []
        isPaired = [False] * n

        for i in range(n):
            if isPaired[i] == False:
                group = [strs[i]]
                for j in range(i + 1, n):
                    if Counter(strs[i]) == Counter(strs[j]):
                        group.append(strs[j])
                        isPaired[j] = True
                isPaired[i] = True

                anagrams.append(group)
        return anagrams
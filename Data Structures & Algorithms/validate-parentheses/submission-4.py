class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        b_map = {"(": ")", "{": "}", "[": "]"}
        for char in s:
            if char in b_map:
                stk.append(char)
            else:
                if stk==[] or b_map[stk.pop()] != char:
                    return False

        return stk==[] 
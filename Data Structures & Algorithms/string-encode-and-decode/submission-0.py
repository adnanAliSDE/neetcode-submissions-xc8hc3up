class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = "\u20b9"
        res = ""
        for word in strs:
            res += word + delimiter
        return res

    def decode(self, s: str) -> List[str]:
        delimiter = "\u20b9"

        res = []
        word = ""
        for char in s:
            if char == delimiter:
                res.append(word)
                word = ""
            else:
                word += char
        return res
class Solution:
    def numDecodings(self, s: str) -> int:
        a, b = 0, 1
        ways = 0
        for idx, char in enumerate(s):
            ways = 0
            # Individual character
            if int(char) >= 1:
                ways += b

            # Pair
            if idx > 0 and 10 <= int(s[idx - 1 : idx + 1]) <= 26:
                ways += a

            a = b
            b = ways

        return ways

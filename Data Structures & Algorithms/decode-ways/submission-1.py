class Solution:
    def numDecodings(self, s: str) -> int:
        a, b = 0, 1
        ways = 0
        for idx, char in enumerate(s, start=2):
            ways = 0
            # Individual character
            if int(char) >= 1:
                ways += b

            # Pair
            s_idx = idx - 2
            pair = s[s_idx - 1 : s_idx + 1]
            if pair.isdigit() and 10 <= int(pair) <= 26:
                ways += a

            a = b
            b = ways

        return ways

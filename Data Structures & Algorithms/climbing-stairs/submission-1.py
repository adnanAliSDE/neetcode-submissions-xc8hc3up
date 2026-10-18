class Solution:
    def climbStairs(self, n: int) -> int:
        def stairs(n, memo=[]):
            if n <= 2:
                return n

            if memo == []:
                memo = [0 for _ in range(n + 1)]
                memo[1]=1
                memo[2]=2

            a, b = memo[n - 1], memo[n - 2]
            if not a:
                a = stairs(n - 1, memo)
            if not b:
                b = stairs(n - 2, memo)
            memo[n] = a + b
            return memo[n]
        return stairs(n)
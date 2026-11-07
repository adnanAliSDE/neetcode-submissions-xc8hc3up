class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        self.denominations = {}

        def helper(amount):
            if not amount:
                return 0

            d = self.denominations.get(amount, None)
            if d is not None:
                return d

            res = float("inf")
            for coin in coins:
                if coin > amount:
                    continue

                else:
                    d = 1
                    d += helper(amount - coin)
                    if not d:
                        continue
                    res = min(d, res)

            if res == float("inf"):
                res = -1

            self.denominations[amount] = res
            return res

        return helper(amount)

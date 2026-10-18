class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = 0
        b = 0
        val=0
        for i in range(2, len(cost)+1):
            val = min(a + cost[i - 1], b + cost[i - 2])
            b = a
            a = val

        return val

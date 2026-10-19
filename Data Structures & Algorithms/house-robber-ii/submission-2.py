class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)
        if n == 4:
            return max(nums[0] + nums[2], nums[1] + nums[3])

        table = nums[:3]
        table[-1] += nums[0]

        refer_start = [True, False, True]
        for i in range(3, n):
            prev_1 = i - 2
            prev_2 = i - 3

            max_candidate, min_candidate = prev_1, prev_2

            if table[prev_1] < table[prev_2]:
                max_candidate, min_candidate = min_candidate, max_candidate

            if refer_start[max_candidate]:
                refer_start.append(True)
            else:
                refer_start.append(False)

            val = table[max_candidate] + nums[i]

            if i == n - 1 and refer_start[i] == True:
                if refer_start[min_candidate]:
                    val = nums[i] + max(table[min_candidate], table[max_candidate]) - nums[0]
                else:
                    val = nums[i] + max(table[min_candidate], table[max_candidate] - nums[0])

            table.append(val)
        return max(table)

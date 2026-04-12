class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ex = {}
        sx = {}

        for num in nums:
            succ = num + 1
            pred = num - 1

            end_with_pred = ex.pop(pred, None)
            start_with_succ = sx.pop(succ, None)

            if end_with_pred is None and start_with_succ is None:
                if not sx.get(num, None) and not ex.get(num, None):
                    sx[num] = num
                    ex[num] = num
            elif end_with_pred is not None and start_with_succ is not None:
                start = end_with_pred
                end = start_with_succ
                ex[end] = start
                sx[start] = end

            elif end_with_pred is not None:

                ex[num] = end_with_pred
                sx[end_with_pred] = num
            else:

                sx[num] = start_with_succ
                ex[start_with_succ] = num

        max_elems = 0

        for start, end in sx.items():
            if end - start + 1 > max_elems:
                max_elems = end - start + 1
                seq = [start, end]

        return max_elems
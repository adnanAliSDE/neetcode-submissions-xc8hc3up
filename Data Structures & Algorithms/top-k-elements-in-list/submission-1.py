class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # 1. create num:freq hashmap
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1

        # 2. Use hashmap to create an array of freq_buckets
        freq_bucket = [[] for _ in range(n)]
        for num, count in counts.items():
            freq_bucket[count - 1].append(
                num
            )  # Arrays have 0 based indexing and no element has 0 freq.

        # 3. Generate the response
        res = []

        for bucket in freq_bucket[::-1]:
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res


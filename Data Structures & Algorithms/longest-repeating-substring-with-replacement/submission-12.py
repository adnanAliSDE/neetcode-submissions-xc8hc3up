class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, max_len = 0, 0, 0
        n = len(s)

        current_char = s[0]
        remaining_replacements = k

        replacement_queue = []

        while r < n or replacement_queue != []:
            char = s[r] if r < n else None

            if char == current_char and char is not None:
                max_len = max(max_len, r - l + 1)
                r += 1
            elif char != current_char and remaining_replacements > 0 and char is not None:
                max_len = max(max_len, r - l + 1)
                remaining_replacements -= 1
                if r not in replacement_queue:
                    replacement_queue.append(r)
                r += 1

            else:
                l = r = (
                    replacement_queue.pop(0) if k > 0 and replacement_queue != [] else r
                )
                remaining_replacements = k
                max_len = max(max_len, r - l + 1)
                current_char = s[r]

            while r == n and remaining_replacements > 0 and l > 0:
                l = l - 1
                remaining_replacements -= 1
                max_len = max(max_len, r - l)

        return max_len
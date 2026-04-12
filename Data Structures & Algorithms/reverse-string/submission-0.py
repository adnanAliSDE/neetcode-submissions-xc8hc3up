class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        forward=0
        backward=len(s)-1

        while forward!=backward:
            s[forward],s[backward]=s[backward],s[forward]
            forward+=1
            backward-=1

            if backward<forward:
                break

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_head = ListNode()
        curr = res_head

        carry = 0
        c1, c2 = l1, l2
        while c1 or c2:
            s = carry
            if c1:
                s += c1.val
                c1 = c1.next

            if c2:
                s += c2.val
                c2 = c2.next

            carry = s // 10
            curr.next = ListNode(s % 10)
            curr = curr.next
        if carry!=0:
            curr.next=ListNode(carry)
        return res_head.next

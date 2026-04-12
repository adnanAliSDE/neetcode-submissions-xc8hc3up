# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        if not headA or not headB:
            return

        if headA == headB:
            return headA

        hashmap = {}

        curr1 = headA
        while curr1:
            hashmap[curr1] = curr1
            curr1 = curr1.next

        curr2 = headB
        while curr2:
            if hashmap.get(curr2, None):
                return curr2
            curr2 = curr2.next
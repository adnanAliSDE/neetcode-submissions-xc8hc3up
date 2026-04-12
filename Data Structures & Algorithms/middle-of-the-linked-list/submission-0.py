# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        n=0
        while curr:
            n+=1
            curr=curr.next

        i=0
        curr=head
        while i<n//2:
            curr=curr.next
            i+=1
        return curr   
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        tail=head
        list_len=1
        while tail.next:
            tail=tail.next
            list_len+=1
        
        curr=head
        index=0
        if list_len-index==n:
            prev=head
            head=head.next
            del prev
            return head

        prev=head
        curr=prev.next
        index=1
        while curr:
            if list_len-index==n:
                prev.next=curr.next
                del curr
                return head
            index+=1
            prev=prev.next
            curr=curr.next
        
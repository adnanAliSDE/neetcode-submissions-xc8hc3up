# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr1=headA
        curr2=headB
        n1,n2=0,0

        while curr1:
            n1+=1
            curr1=curr1.next
        
        while curr2:
            n2+=1
            curr2=curr2.next
        
        diffA=n1-n2
        curr1=headA
        while diffA>0:
            curr1=curr1.next
            diffA-=1
        
        diffB=n2-n1
        curr2=headB
        while diffB>0:
            curr2=curr2.next
            diffB-=1
        
        while curr1!=curr2:
            curr1=curr1.next
            curr2=curr2.next
        return curr1

        
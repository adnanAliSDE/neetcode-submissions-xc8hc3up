# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n1=len(lists)
        n=n1
        for i in range(n1):
            if lists[i]==None:
                lists.pop(i)
                n=n-1
        if n==0:
            return None

        def get_min_idx(ptrs):
            min_ptr_idx=0
            for i in range(len(ptrs)):
                if ptrs[i].val<ptrs[min_ptr_idx].val:
                    min_ptr_idx=i
            return min_ptr_idx

        min_ptr_idx=get_min_idx(lists)
        head=ListNode(lists[min_ptr_idx].val)
        curr=head
        
        if  lists[min_ptr_idx].next==None:
                lists.pop(min_ptr_idx)
        else:
                lists[min_ptr_idx]=lists[min_ptr_idx].next

        while lists!=[]:
            min_ptr_idx=get_min_idx(lists)
            curr.next=ListNode(lists[get_min_idx(lists)].val)
            curr=curr.next

            if  lists[min_ptr_idx].next==None:
                lists.pop(min_ptr_idx)
            else:
                lists[min_ptr_idx]=lists[min_ptr_idx].next
        return head

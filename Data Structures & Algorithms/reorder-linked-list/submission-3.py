class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        tail_pred = head
        if head is None or head.next is None or head.next.next is None:
            return

        while tail_pred.next.next is not None:
            tail_pred = tail_pred.next

        while True:
            succ = curr.next
            tail = tail_pred.next
            tail.next = succ
            curr.next = tail

            tail_pred.next = None

            tail_pred = succ

            if tail_pred.next is not None:
                while tail_pred.next.next is not None:
                    tail_pred = tail_pred.next

            curr = succ
            if curr == tail_pred:
                break
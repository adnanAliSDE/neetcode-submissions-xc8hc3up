class Solution:
    def mergeTwoLists(
        self, h1: Optional[ListNode], h2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not h1 and not h2:
            return None
        elif not h1:
            merged = ListNode(h2.val)
            h2 = h2.next
        elif not h2:
            merged = ListNode(h1.val)
            h1 = h1.next
        elif h1.val > h2.val:
            merged = ListNode(h2.val)
            h2 = h2.next
        else:
            merged = ListNode(h1.val)
            h1 = h1.next

        curr = merged
        while h1 or h2:
            if h1 is None:
                curr.next = ListNode(h2.val)
                curr = curr.next
                h2 = h2.next

            elif h2 is None:
                curr.next = ListNode(h1.val)
                curr = curr.next
                h1 = h1.next
            else:
                if h1.val > h2.val:
                    curr.next = ListNode(h2.val)
                    curr = curr.next
                    h2 = h2.next

                elif h1.val < h2.val:
                    curr.next = ListNode(h1.val)
                    curr = curr.next
                    h1 = h1.next
                else:
                    curr.next = ListNode(h1.val)
                    curr = curr.next
                    curr.next = ListNode(h2.val)
                    curr = curr.next
                    h1 = h1.next
                    h2 = h2.next

        return merged

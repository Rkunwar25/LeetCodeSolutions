class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)   # dummy head of sorted list
        curr = head

        while curr:
            next_node = curr.next  # save next node

            # find position to insert curr
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # insert curr between prev and prev.next
            curr.next = prev.next
            prev.next = curr

            curr = next_node

        return dummy.next

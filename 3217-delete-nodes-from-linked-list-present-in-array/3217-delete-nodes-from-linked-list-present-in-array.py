class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        remove_set = set(nums)

        dummy = ListNode(0)
        tail = dummy
        curr = head

        while curr:
            if curr.val not in remove_set:
                tail.next = ListNode(curr.val)
                tail = tail.next
            curr = curr.next

        return dummy.next

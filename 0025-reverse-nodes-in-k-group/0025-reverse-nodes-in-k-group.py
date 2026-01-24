class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Check if k nodes exist
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1
        
        if count < k:
            return head   # not enough nodes to reverse

        # Step 2: Reverse k nodes
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: Recursive call for remaining list
        head.next = self.reverseKGroup(curr, k)

        return prev

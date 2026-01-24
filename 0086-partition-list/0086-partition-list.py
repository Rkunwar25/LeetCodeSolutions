# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
#         l=[]
#         n=head
#         while n:
#             l.append(n.val)
#             n=n.next
#         newl=[]
#         some=[]
#         for i in l:
#             if i<x:
#                 newl.append(i)
#             else:
#                 some.append(i)
#         newl.extend(some)
#         new=None
#         tail=None
#         for i in newl:
#             n=ListNode(i)
#             if new is None:
#                 new=n
#                 tail=n
#             else:
#                 tail.next=n
#                 tail=n
#         return new
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = ListNode(0)
        after = ListNode(0)

        b = before
        a = after

        while head:
            if head.val < x:
                b.next = head
                b = b.next
            else:
                a.next = head
                a = a.next
            head = head.next

        a.next = None          # Important to avoid cycle
        b.next = after.next   # Join the two lists

        return before.next

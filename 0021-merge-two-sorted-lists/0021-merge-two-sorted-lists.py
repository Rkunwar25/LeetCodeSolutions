# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         l1=[]
#         l2=[]
#         n=list1
#         while n:
#             l1.append(n.val)
#             n=n.next        
#         n=list2
#         while n:
#             l2.append(n.val)
#             n=n.next        
#         l=sorted(l1+l2)
#         new=None
#         tail=None
#         for i in l:
#             n=ListNode(i)
#             if new is None:
#                 new=n
#                 tail=n
#             else:
#                 tail.next=n
#                 tail=n
#         return new       
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach remaining nodes
        tail.next = list1 if list1 else list2

        return dummy.next

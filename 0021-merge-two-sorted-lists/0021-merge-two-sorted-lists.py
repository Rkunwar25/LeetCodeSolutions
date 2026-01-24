# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=[]
        l2=[]
        n=list1
        while n:
            l1.append(n.val)
            n=n.next        
        n=list2
        while n:
            l2.append(n.val)
            n=n.next        
        l=sorted(l1+l2)
        new=None
        tail=None
        for i in l:
            n=ListNode(i)
            if new is None:
                new=n
                tail=n
            else:
                tail.next=n
                tail=n
        return new       
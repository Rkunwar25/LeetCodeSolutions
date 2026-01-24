# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l=[]
        l2=[]
        n=list1        
        while n:
            l.append(n.val)
            n=n.next
        n=list2      
        while n:
            l2.append(n.val)
            n=n.next
        newl=l[:a]+l2+l[b+1:]
        new=None
        tail=None
        for i in newl:
            n=ListNode(i)
            if new is None:
                new=n
                tail=n
            else:
                tail.next=n
                tail=n
        return new    
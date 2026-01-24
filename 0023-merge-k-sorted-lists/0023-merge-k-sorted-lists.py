# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l=[]
        for head in lists:
            curr=head
            while curr:
                l.append(curr.val)
                curr=curr.next
        l=sorted(l)
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
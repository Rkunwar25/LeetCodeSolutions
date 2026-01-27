# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=1
        n=head
        l=[]
        while n:
            l.append(n.val)
            n=n.next
        i=0
        while i<len(l):
            if len(l[i:i+c])%2==0:
                l[i:i+c]=l[i:i+c][::-1] 
            i+=c
            c+=1
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
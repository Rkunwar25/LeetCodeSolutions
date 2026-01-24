# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        l=[]
        l.append(head.val)
        while head.next:
            a=head.val
            # l.append(a)
            head=head.next
            b=head.val
            g=gcd(a,b)
            l.extend([g,b])
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
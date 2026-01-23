# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l=[]
        n=head
        while n:
            l.append(n.val)
            n=n.next
        x=l[left-1:right]
        x=x[::-1]
        l=l[:left-1]+x+l[right:]
        newnode=None
        tail=None
        for i in l:
            n=ListNode(i)
            if newnode is None:
                newnode=n
                tail=n
            else:
                tail.next=n
                tail=n
        return newnode
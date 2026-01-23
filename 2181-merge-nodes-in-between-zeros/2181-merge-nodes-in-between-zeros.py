# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        n=head
        while n:
            l.append(n.val)
            n=n.next
        stack=[]
        s=0
        for i in l:
            if i!=0:
                s+=i
            else:
                stack.append(s)
                s=0
        if 0 in stack:
            stack.remove(0)
        newnode=None
        tail=None
        for i in stack:
            n=ListNode(i)
            if newnode is None:
                newnode=n
                tail=n
            else:
                tail.next=n
                tail=n
        return newnode     
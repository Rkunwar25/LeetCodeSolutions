# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=[]
        node=head
        while node:
            l.append(node.val)
            node=node.next
        if len(l)!=0:
            k=k%len(l)
        l=l[-k:]+l[:-k]
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
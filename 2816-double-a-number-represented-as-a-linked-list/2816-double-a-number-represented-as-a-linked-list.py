# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys
sys.set_int_max_str_digits(0)  # 0 = unlimited

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=""
        n=head
        while n:
            s+=str(n.val)
            n=n.next
        s=str(int(s)*2)
        print(s)
        s=list(map(int,list(s)))
        nn=None
        t=None
        for i in s:
            n=ListNode(i)
            if nn is None:
                nn=n
                t=n
            else:
                t.next=n
                t=n
        return nn
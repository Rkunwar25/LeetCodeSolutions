# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        l=[]
        temp=head
        while temp:
            l.append(temp.val)
            temp=temp.next
        l1=[]
        for i in l:
            if l.count(i)==1:
                l1.append(i)
        print(l1)
        if not l1:
            return 
        head = ListNode(l1[0])
        
        current = head
        for val in l1[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def create_linked_list(arr):
    if not arr:
        return None

    head = ListNode(int(arr[0]))
    current = head

    for val in arr[1:]:
        current.next = ListNode(int(val))
        current = current.next

    return head

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        ans=int("".join(map(str,s1)))+int("".join(map(str,s2)))
        ans=list(str(ans)) 
        return create_linked_list(ans)
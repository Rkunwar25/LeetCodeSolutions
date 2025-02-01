struct ListNode* oddEvenList(struct ListNode* head) {
    if (head == NULL || head->next == NULL || head->next->next == NULL)
        return head;

    struct ListNode* odd = head;  // Head of the odd list
    struct ListNode* even = head->next;  // Head of the even list
    struct ListNode* evenHead = even;  // Save the head of the even list for later connection

    // Traverse the list, rearranging the odd and even nodes
    while (even != NULL && even->next != NULL) {
        odd->next = odd->next->next;  // Skip the next even node
        even->next = even->next->next;  // Skip the next odd node
        
        odd = odd->next;  // Move odd pointer
        even = even->next;  // Move even pointer
    }

    // Connect the odd list to the even list
    odd->next = evenHead;

    return head;
}

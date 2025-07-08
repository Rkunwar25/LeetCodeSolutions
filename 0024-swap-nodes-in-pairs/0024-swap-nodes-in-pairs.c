struct ListNode* swapPairs(struct ListNode* head) {
    if (!head || !head->next) return head; // base cases

    struct ListNode *temp = head;
    struct ListNode *newHead = head->next; // second node becomes new head
    struct ListNode *prev = NULL;

    while (temp && temp->next) {
        struct ListNode *n = temp->next;    // second node in pair
        struct ListNode *t = n->next;       // node after the pair

        // Swapping
        n->next = temp;
        temp->next = t;

        // Connect previous swapped pair to current
        if (prev != NULL) {
            prev->next = n;
        }

        // Move to next pair
        prev = temp;
        temp = t;
    }

    return newHead;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int s1[10000], s2[10000];
    int top1 = 0, top2 = 0;

    // Push values of l1 into stack
    while (l1) {
        s1[top1++] = l1->val;
        l1 = l1->next;
    }

    // Push values of l2 into stack
    while (l2) {
        s2[top2++] = l2->val;
        l2 = l2->next;
    }

    int carry = 0;
    struct ListNode* head = NULL;

    while (top1 > 0 || top2 > 0 || carry) {
        int sum = carry;

        if (top1 > 0) sum += s1[--top1];
        if (top2 > 0) sum += s2[--top2];

        struct ListNode* node = malloc(sizeof(struct ListNode));
        node->val = sum % 10;
        node->next = head;
        head = node;

        carry = sum / 10;
    }

    return head;
}

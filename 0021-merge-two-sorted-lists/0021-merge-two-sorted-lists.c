struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    // If either list is empty, return the other
    if (!list1) return list2;
    if (!list2) return list1;

    // Decide the head of the merged list
    struct ListNode* head = NULL;
    if (list1->val < list2->val) {
        head = list1;
        list1 = list1->next;
    } else {
        head = list2;
        list2 = list2->next;
    }

    // `tail` will build the rest of the list
    struct ListNode* tail = head;

    while (list1 && list2) {
        if (list1->val < list2->val) {
            tail->next = list1;
            list1 = list1->next;
        } else {
            tail->next = list2;
            list2 = list2->next;
        }
        tail = tail->next;
    }

    // Attach the remaining part
    tail->next = list1 ? list1 : list2;

    return head;
}

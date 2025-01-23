/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    int count=0;
    struct ListNode * temp=head;
    struct ListNode * newtemp=head;
    struct ListNode * prev=head;
    while(temp!=NULL)
    {
        count++;
        temp=temp->next;
    }
    int c=0;
    if(n==count)
    {
        return head=head->next;
    }
    while(c<(count-n))
    {
        prev=newtemp;
        newtemp=newtemp->next;
        c++;
    }
    prev->next=newtemp->next;
    newtemp->next=NULL;
    return head;
    free(newtemp);
    
}
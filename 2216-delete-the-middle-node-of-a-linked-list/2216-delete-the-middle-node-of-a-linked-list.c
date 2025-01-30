/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteMiddle(struct ListNode* head) {
    int n=0;
    struct ListNode* temp=head;
    while(temp!=NULL)
    {
        n++;
        temp=temp->next;
    }
    struct ListNode* prev=head;
    struct ListNode* newtemp=head;
    int mid=(n/2)+1;
    if(n==1)
    {
        return head=head->next;
    }
    int count=0;
    while(count<mid-1)
    {
        prev=newtemp;
        newtemp=newtemp->next;
        count++;
    }
    prev->next=newtemp->next;
    newtemp->next=NULL;
    free(newtemp);
    return head;
    
}
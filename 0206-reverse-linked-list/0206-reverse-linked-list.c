/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    if(head==NULL)
    {
        return NULL;
    }
    int n=0,i;
    struct ListNode* temp=head;
    struct ListNode* temp2=head;
    while(temp!=NULL)
    {
        n++;
        temp=temp->next;
    }
    int *arr=(int*)malloc(n*sizeof(int));
    for (i=0;i<n;i++)
    {
        arr[i]=temp2->val;
        temp2=temp2->next;
    }
    temp=head;
    for(i=n-1;i>=0;i--)
    {
        temp->val=arr[i];
        temp=temp->next;
    }
    return head;
    
}
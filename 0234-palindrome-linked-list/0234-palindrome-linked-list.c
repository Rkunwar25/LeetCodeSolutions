/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head) {
    int c=0;
    struct ListNode *temp=head;
    while(temp)
    {
       c++;
       temp=temp->next;
    }
    free(temp);
    int *p=(int*)malloc(c*sizeof(int));
    temp=head;
    int i=0;
    while(temp)
    {
        p[i++]=temp->val;
        temp=temp->next;
    }
    int j=c-1;
    for(i=0;i<c/2;i++,j--)
    {
        if(p[i]!=p[j])
        return false;
    }
    return true;
}
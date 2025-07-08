/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 #include<math.h>
int getDecimalValue(struct ListNode* head) {
    int c=0;
    struct ListNode *temp=head;
    while(temp)
    {
        c++;
        temp=temp->next;
    }
    int *p=(int*)malloc(c*sizeof(int));
    free(temp);
    temp=head;
    int i=0;
    while(temp)
    {
        p[i++]=temp->val;
        temp=temp->next;
    }
    free(temp);
    int pw=0,val=0;
    for(i=c-1;i>=0;i--)
    {
        val+=pow(2,pw)*p[i];
        pw++;   
    } 
    return val;

}
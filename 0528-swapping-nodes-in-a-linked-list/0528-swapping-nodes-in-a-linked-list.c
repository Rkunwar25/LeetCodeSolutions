/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapNodes(struct ListNode* head, int k) {
     int c=0;
     struct ListNode *t=head;
     struct ListNode *n=head;
     while(t)
     {
        c++;
        t=t->next;
     }
     
     t=head;
     int c1=1,c2=1;
     while(c1<k)
     {
        t=t->next;
        c1++;
     }
     while(c2<(c-k+1))
     {
        n=n->next;
        c2++;
     }
     int temp=t->val;
     t->val=n->val;
     n->val=temp;
     return head;
}
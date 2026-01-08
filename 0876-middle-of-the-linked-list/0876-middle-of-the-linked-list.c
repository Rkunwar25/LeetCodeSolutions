/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    int l=0;
    struct ListNode* temp=head;
    while(temp){
        l++;
        temp=temp->next;
    }
   
    int mid=l/2;
    struct ListNode* temp2=head;
    int c=0;
    while (c<mid){
        c++;
        temp2=temp2->next;
    }
    return temp2;
}
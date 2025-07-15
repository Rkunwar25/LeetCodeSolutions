/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
int i=0;
    TreeNode* helper(vector<int>& preorder,int ub)
    {   
        if(i<preorder.size() && preorder[i]<ub){
        int x=preorder[i];
        TreeNode* root=new TreeNode(preorder[i++]);
        root->left=helper(preorder,x);
        root->right=helper(preorder,ub);
        return root;
    }
    return NULL;
}
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        return helper(preorder,1001);
    }
};
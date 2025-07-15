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
    map<int,int> mp;
    TreeNode* construct(vector<int>& preorder,int ps,int pe,vector<int>& inorder,int is,int ie)
    {
        if(ps<=pe){
         TreeNode* root=new TreeNode(preorder[ps]);
         int ri=mp[preorder[ps]];
         int nl=ri-is;
         root->left=construct(preorder,ps+1,ps+nl,inorder,is,ri-1);
         root->right=construct(preorder,ps+nl+1,pe,inorder,ri+1,ie);
         return root;

    }
    return NULL;
    }
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int n=preorder.size();
        for(int i=0;i<n;i++)
        {
            mp[inorder[i]]=i;
        }
        return construct(preorder,0,n-1,inorder,0,n-1);

    }
};
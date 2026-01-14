/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool hasPathSum(struct TreeNode* root, int targetSum) {
    // Base case: empty tree
    if (root == NULL)
        return false;

    // If leaf node, check sum
    if (root->left == NULL && root->right == NULL) {
        return root->val == targetSum;
    }

    // Recur for left or right subtree
    return hasPathSum(root->left, targetSum - root->val) ||
           hasPathSum(root->right, targetSum - root->val);
}

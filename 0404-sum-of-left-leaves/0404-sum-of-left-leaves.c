int sumOfLeftLeaves(struct TreeNode* root) {
    if (root == NULL) return 0;

    int sum = 0;

    // Check if left child exists and is a leaf
    if (root->left && root->left->left == NULL && root->left->right == NULL) {
        sum += root->left->val;
    }

    // Recurse into left and right subtrees
    sum += sumOfLeftLeaves(root->left);
    sum += sumOfLeftLeaves(root->right);

    return sum;
}

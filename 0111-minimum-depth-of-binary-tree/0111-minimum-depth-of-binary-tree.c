int minDepth(struct TreeNode* root) {
    if (root == NULL)
        return 0;

    // If one child is NULL, return depth of the other child
    if (root->left == NULL)
        return 1 + minDepth(root->right);
    if (root->right == NULL)
        return 1 + minDepth(root->left);

    // If both children exist, take minimum
    int left = minDepth(root->left);
    int right = minDepth(root->right);

    return 1 + (left < right ? left : right);
}

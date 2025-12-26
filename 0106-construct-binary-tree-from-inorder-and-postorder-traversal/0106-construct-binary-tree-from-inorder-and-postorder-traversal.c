/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 int findIndex(int* inorder, int start, int end, int value) {
    for (int i = start; i <= end; i++) {
        if (inorder[i] == value)
            return i;
    }
    return -1;
}

struct TreeNode* build(
    int* inorder, int inStart, int inEnd,
    int* postorder, int postStart, int postEnd
) {
    if (inStart > inEnd || postStart > postEnd)
        return NULL;

    // Root is last element in postorder
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = postorder[postEnd];
    root->left = root->right = NULL;

    int rootIndex = findIndex(inorder, inStart, inEnd, root->val);
    int leftSize = rootIndex - inStart;

    // Build left and right subtrees
    root->left = build(
        inorder, inStart, rootIndex - 1,
        postorder, postStart, postStart + leftSize - 1
    );

    root->right = build(
        inorder, rootIndex + 1, inEnd,
        postorder, postStart + leftSize, postEnd - 1
    );

    return root;
}

struct TreeNode* buildTree(int* inorder, int inorderSize, int* postorder, int postorderSize) {
    if (!inorder || !postorder || inorderSize == 0)
        return NULL;

    return build(
        inorder, 0, inorderSize - 1,
        postorder, 0, postorderSize - 1
    );
}
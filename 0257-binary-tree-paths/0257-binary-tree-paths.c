#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Definition for a binary tree node.
 */
// struct TreeNode {
//     int val;
//     struct TreeNode *left;
//     struct TreeNode *right;
// };

/* Helper DFS function */
void dfs(struct TreeNode* root, char* path, char** res, int* returnSize) {
    if (!root) return;

    char buffer[20];
    sprintf(buffer, "%d", root->val);

    int len = strlen(path);
    if (len != 0) {
        strcat(path, "->");
    }
    strcat(path, buffer);

    // If leaf node, store the path
    if (!root->left && !root->right) {
        res[*returnSize] = strdup(path);
        (*returnSize)++;
        path[len] = '\0';   // backtrack
        return;
    }

    dfs(root->left, path, res, returnSize);
    dfs(root->right, path, res, returnSize);

    path[len] = '\0';  // backtrack
}

char** binaryTreePaths(struct TreeNode* root, int* returnSize) {
    *returnSize = 0;
    if (!root) return NULL;

    // Max paths ≤ number of nodes (safe upper bound)
    char** res = (char**)malloc(sizeof(char*) * 1000);

    char path[1000] = "";
    dfs(root, path, res, returnSize);

    return res;
}

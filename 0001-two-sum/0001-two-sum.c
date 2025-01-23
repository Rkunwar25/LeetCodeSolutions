/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    *returnSize=2;
    int * sol = (int*)malloc(2 * sizeof(int));
    sol[0]=-1;
    sol[1]=-1;
    int i,j,sum;
    for(i=0;i<numsSize;i++)
    {
        sum=nums[i];
        for(j=i+1;j<numsSize;j++)
        {
            if(sum+nums[j]==target)
            {
                sol[0]=i;
                sol[1]=j;
                return sol;
            }
        }
    }
    return sol;
}
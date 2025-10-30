// class Solution {
//     public void moveZeroes(int[] nums) {
//         for(int i=0;i<nums.length-1;i++){
//             for(int j=0;j<nums.length-i-1;j++){
//                 if(nums[j]==0 && nums[j+1]!=0){
//                     int temp=nums[j];
//                     nums[j]=nums[j+1];
//                     nums[j+1]=temp;
//                 }
//             }
//         }
//     }
// }
class Solution {
    public void moveZeroes(int[] nums) {
        int index = 0; // position to place the next non-zero

        // Step 1: Move all non-zero elements forward
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[index++] = nums[i];
            }
        }

        // Step 2: Fill remaining positions with zeros
        while (index < nums.length) {
            nums[index++] = 0;
        }
    }
}

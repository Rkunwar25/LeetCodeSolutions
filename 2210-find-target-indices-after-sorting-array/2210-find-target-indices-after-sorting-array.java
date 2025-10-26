class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        Arrays.sort(nums);
        List<Integer> targ=new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            if (target==nums[i]){
                targ.add(i);
            }
        }
        return targ;
    }
}
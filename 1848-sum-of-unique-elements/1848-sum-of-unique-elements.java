import java.util.HashMap;

class Solution {
    public int sumOfUnique(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        
        // Count occurrences of each number
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        
        int sum = 0;
        // Sum elements that occur exactly once
        for (int key : map.keySet()) {
            if (map.get(key) == 1) {
                sum += key;
            }
        }
        
        return sum;
    }
}
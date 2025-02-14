/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    if (!nums.includes(1)) return 0; // Edge case: No 1s in the array

    let s = nums.join('');
    let x = s.split(/[^1]/); // Split by non-1 characters

    return Math.max(...x.map(str => str.length)); // Get the longest sequence length
};

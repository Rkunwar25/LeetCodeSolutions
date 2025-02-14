/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    if (!nums.includes(1)) return 0; // Edge case: No 1s in the array

    var s = nums.join('');
    var x = s.split(/[^1]/); // Split by non-1 characters
    var maxsize=x[0].length;
    for (let i=1;i<x.length;i++)
    {
        if(x[i].length>maxsize)
          maxsize=x[i].length
    }
    return maxsize

};

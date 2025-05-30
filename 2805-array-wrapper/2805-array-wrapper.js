/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(nums) {
    this.nums = nums;

    this.valueOf = function() {
        return this.nums.reduce((acc, val) => acc + val, 0);
    };

    this.toString = function() {
        return `[${this.nums.join(',')}]`;
    };
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
    
}

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
    
}

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */
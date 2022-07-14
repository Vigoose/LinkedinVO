/*
 * @lc app=leetcode id=53 lang=java
 *
 * [53] Maximum Subarray
 */

// @lc code=start
class Solution {
    public int maxSubArray(int[] nums) {
        int preSum = nums[0];
        int result = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int curMax = preSum < 0 ? nums[i] : nums[i] + preSum;
            preSum = curMax;
            result = Math.max(curMax, result);
        }

        return result;
    }
}
// @lc code=end


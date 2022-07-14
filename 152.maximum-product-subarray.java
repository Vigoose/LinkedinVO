/*
 * @lc app=leetcode id=152 lang=java
 *
 * [152] Maximum Product Subarray
 */

// @lc code=start
class Solution {
    public int maxProduct(int[] nums) {
        int maxTillNow = nums[0];
        int minTillNow = nums[0];
        int result = nums[0];

        for (int i = 1; i < nums.length; i++) {
            int temp = maxTillNow;
            maxTillNow = Math.max(nums[i], Math.max(maxTillNow * nums[i], minTillNow * nums[i]));
            minTillNow = Math.min(nums[i], Math.min(temp * nums[i], minTillNow * nums[i]));

            if (maxTillNow > result) {
                result = maxTillNow;
            }
        }

        return result;
    }
}
// @lc code=end


/*
 * @lc app=leetcode id=34 lang=java
 *
 * [34] Find First and Last Position of Element in Sorted Array
 * 
 * 
 * 
 * 
 * [5,7,7,8,8,10]
 *  0 1 2 3 4 5
 *        l r
 *        m    
 * 
 * 
 *  
 * 
 * 
 * 
 * 
 * 
 * 
 */

// @lc code=start
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] res = new int[] { -1, -1 };
        if (nums == null || nums.length == 0)
            return res;

        // find the first position
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                // find target
                if (mid == 0 || nums[mid] != nums[mid - 1]) {
                    res[0] = mid;
                    break;
                } else {
                    right = mid - 1;
                }
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        if (res[0] == -1)
            return res;
        // find the last position
        left = 0;
        right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                // find target
                if (mid == nums.length - 1 || nums[mid] != nums[mid + 1]) {
                    res[1] = mid;
                    break;
                } else {
                    left = mid + 1;
                }

            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return res;
    }
}
// @lc code=end

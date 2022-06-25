import java.util.Random;

/*
 * @lc app=leetcode id=215 lang=java
 *
 * [215] Kth Largest Element in an Array
 */

// @lc code=start
class Solution {
    public int findKthLargest(int[] nums, int k) {
        if (nums == null || nums.length == 0) {
            return -1;
        }

        
    }


    private int findPosition(int[] nums, int start, int end) {
        Random rd = new Random();
        int pivotIndex = rd.nextInt(start + end);
        int pivot = nums[pivotIndex];
        int i = start;
        int j = end;
        swap(nums, pivotIndex, j);
        j--;
        int k = i;
        while (k <= j) {
            if (nums[k] > pivot) {
                swap(nums, k, i);
                k++;
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
// @lc code=end


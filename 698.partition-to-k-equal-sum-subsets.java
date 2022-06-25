/*
 * @lc app=leetcode id=698 lang=java
 *
 * [698] Partition to K Equal Sum Subsets
 */

// @lc code=start
class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }

        if (sum % k != 0) {
            return false;
        }

        sum /= k;

        Arrays.sort(nums);

        return dfs(nums, k, sum, 0, nums.length - 1, new boolean[nums.length]);
    }

    private boolean dfs(int[] nums, int k, int target, int currentSum, int index, boolean[] visited) {
        if (k == 0) {
            return true;
        }

        if (currentSum == target) {
            return dfs(nums, k - 1, target, 0, nums.length - 1, visited);
        }

        for (int i = index; i >= 0; i--) {
            if (visited[i]) continue;

            if (i + 1 < nums.length && !visited[i + 1] && nums[i] == nums[i + 1]) continue;

            if (currentSum + nums[i] > target) continue;

            visited[i] = true;
            if (dfs(nums, k, target, currentSum + nums[i], i - 1, visited)) return true;
            visited[i] = false;
        }

        return false;
    }
}
// @lc code=end


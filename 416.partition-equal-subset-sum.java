import java.util.ArrayList;

/*
 * @lc app=leetcode id=416 lang=java
 *
 * [416] Partition Equal Subset Sum
 */

// @lc code=start
class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0;

        for (int n : nums) {
            sum += n;
        }

        if (sum % 2 != 0) {
            return false;
        }

        for (int i : nums) {
            if (i > sum / 2)
                return false;
        }

        sum /= 2;

        boolean[][] dp = new boolean[nums.length + 1][sum + 1];

        dp[0][0] = true;

        for (int i = 1; i < dp.length; i++) {
            dp[i][0] = true;
        }

        for (int i = 1; i < sum + 1; i++) {
            dp[0][i] = false;
        }

        for (int i = 1; i < dp.length; i++) {
            for (int j = 1; j < sum + 1; j++) {
                dp[i][j] = dp[i - 1][j];

                if (nums[i - 1] <= j) {
                    dp[i][j] = dp[i - 1][j] || dp[i - 1][j - nums[i - 1]];
                }
            }
        }

        return dp[nums.length - 1][sum];
    }
}
// @lc code=end


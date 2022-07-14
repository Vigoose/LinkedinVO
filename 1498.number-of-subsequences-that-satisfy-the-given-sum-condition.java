/*
 * @lc app=leetcode id=1498 lang=java
 *
 * [1498] Number of Subsequences That Satisfy the Given Sum Condition
 */

// @lc code=start
class Solution {
    public int numSubseq(int[] nums, int target) {
        int n = nums.length;
        int mod = 1000000007;
        //record all 2 ^ n to save time
        int[] dp = new int[n + 1];
        dp[0] = 1;
        for (int i = 1; i <= n; ++i) {
            dp[i] = (dp[i - 1] * 2) % mod;
        }
        //sort
        Arrays.sort(nums);
            
        //try to use each number as the min number, fixing min number also makes sure that min number alone will be a valid subsequence
        int ans = 0;
        for (int i = 0, j = n - 1; i <= j;) {
            if (nums[i] + nums[j] > target) { // find the largest number that meets the sum condition
                j--;
            } else {
                //add all possible combinations in [i + 1, j]
                ans = (ans + dp[j - i]) % mod;
                i++;
            }
        }
        return ans;
    }
}
// @lc code=end


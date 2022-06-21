/*
 * @lc app=leetcode id=636 lang=java
 *
 * [636] Exclusive Time of Functions
 */

// @lc code=start
class Solution {
    public int[] exclusiveTime(int n, List<String> logs) {
        
        int prevTime = 0;

        for (String str : logs) {
            int functionName = Integer.valueOf(str.split(":")[0]);
            String event = str.split(":")[1];
            int timestamp = Integer.valueOf(str.split(":")[2]);

            
            
            
        }
    }
}
// @lc code=end


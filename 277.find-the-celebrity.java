/*
 * @lc app=leetcode id=277 lang=java
 *
 * [277] Find the Celebrity
 */

// @lc code=start
/* The knows API is defined in the parent class Relation.
      boolean knows(int a, int b); */

public class Solution extends Relation {
    public int findCelebrity(int n) {
        int result = 0;

        for (int i = 1; i < n; i++) {
            if (!knows(i, result)) {
                result = i;
            }
        }

        for (int i = 0; i < n; i++) {
            if (i == result) continue;

            if (knows(result, i) || !knows(i, result)) {
                return -1;
            }
        }

        return result;
    }
}
// @lc code=end


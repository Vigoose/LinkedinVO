import java.util.HashMap;
import java.util.HashSet;

/*
 * @lc app=leetcode id=149 lang=java
 *
 * [149] Max Points on a Line
 */

// @lc code=start
class Solution {
    public int maxPoints(int[][] points) {
        if (points == null || points.length == 0) {
            return 0;
        }
        int result = 0;
        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 0; i < points.length; i++) {
            map.clear();
            int duplicate = 0;
            int curMax = 0;
            for (int j = i + 1; j < points.length; j++) {
                int deltaX = points[j][0] - points[i][0];
                int deltaY = points[j][1] - points[i][1];

                if (deltaX == 0 && deltaY == 0) {
                    duplicate++;
                    continue;
                }

                int gcd = GCD(deltaX, deltaY);

                deltaX /= gcd;
                deltaY /= gcd;

                String str = deltaX + ":" + deltaY;
                map.put(str, map.getOrDefault(str, 0) + 1);
                curMax = Math.max(curMax, map.get(str));
            }

            result = Math.max(result, curMax + duplicate + 1);
        }

        return result;
    }

    public int GCD(int a, int b) {
        if (b == 0) {
            return a;
        }
        return GCD(b, a % b);
    }
}
// @lc code=end


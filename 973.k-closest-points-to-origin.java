import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

/*
 * @lc app=leetcode id=973 lang=java
 *
 * [973] K Closest Points to Origin
 */

// @lc code=start
class Solution {
    public int[][] kClosest(int[][] points, int k) {
        int start = 0;
        int end = points.length - 1;
        while (start <= end) {
            int index = helper(points, start, end);
            if (index == k) {
                break;
            } 

            if (index < k) {
                start = index + 1;
            }  else {
                end = index - 1;
            }
        }

        return Arrays.copyOfRange(points, 0, k);
    }

    private int helper(int[][] points, int start, int end) {
        int[] pivot = points[start];
        while (start < end) {
            while (start < end && compare(points[start], pivot) <= 0) start++;
            points[end] = points[start];
            while (start < end && compare(points[end], pivot) >= 0) end--;
            points[start] = points[end];
        }
        points[start] = pivot;
        return start;
    }

    public int compare(int[] a, int[] b) {
        return (a[0] * a[0] + a[1] * a[1]) - (b[0] * b[0] + b[1] * b[1]);
    }

}
// @lc code=end


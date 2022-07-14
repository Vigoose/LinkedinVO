import java.util.*;

/**
 * 
 * @lc app=leetcode id=2174 lang=java
 * 
 * 2174. Remove All Ones With Row and Column Flips II
 * You are given a 0-indexed m x n binary matrix grid.
 * In one operation, you can choose any i and j that meet the following 
 * conditions:
 * 0 <= i < m
 * 0 <= j < n
 * grid[i][j] == 1
 * and change the values of all cells in row i and column j to zero.
 * 
 * Return the minimum number of operations needed to remove all 1's from grid.
 * 
 * @lc code=start

 */
class Solution {
    int m = 0;
    int n = 0;
    int ans = Integer.MAX_VALUE;

    public int removeOnes(int[][] grid) {
        m = grid.length;
        n = grid[0].length;
        int[] flips = new int[1];
        backtrack(grid, new HashSet<>(), flips);
        return ans;
    }

    private void backtrack(int[][] grid, HashSet<String> set, int[] flips) {
        boolean allZeros = true;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    String row = "r" + i;
                    String col = "c" + j;

                    if (!set.contains(row) && !set.contains(col)) {
                        allZeros = false;
                        set.add(row);
                        set.add(col);
                        flips[0] += 1;
                        backtrack(grid, set, flips);

                        flips[0] -= 1;
                        set.remove(row);
                        set.remove(col);
                    }
                }
            }
        }

        if (allZeros) {
            ans = Math.min(ans, flips[0]);
        }

    }
}

import java.util.*;

/*
 * @lc app=leetcode id=254 lang=java
 *
 * [254] Factor Combinations
 * 
 * 
 * 
 *          6
 *     2
 * 3
 * 
 * 
 * 
 * 

 */

// @lc code=start
class Solution {
    public List<List<Integer>> getFactors(int n) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        dfs(res, list, n, 2);
        return res;
    }

    private void dfs(List<List<Integer>> res, List<Integer> list, int n, int factor) {
        for (int i = factor; i*i <= n; i++) {
            if (n % i == 0) {
                list.add(i);
                list.add(n/i);
                res.add(new ArrayList<>(list));
                list.remove(list.size() - 1);
                dfs(res, list, n / i, i);
                list.remove(list.size() - 1);
            }
        }
    }
}
// @lc code=end


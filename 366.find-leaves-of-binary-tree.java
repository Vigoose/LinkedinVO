import java.util.ArrayList;

/*
 * @lc app=leetcode id=366 lang=java
 *
 * [366] Find Leaves of Binary Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> findLeaves(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(root, res);
        return res;
    }

    private int dfs(TreeNode root, List<List<Integer>> res) {
        if (root == null) {
            return 0;
        }

        int leftHeight = dfs(root.left, res);
        int rightHeight = dfs(root.right, res);

        int curHeight = Math.max(leftHeight, rightHeight);
        if (curHeight == res.size()) {
            res.add(new ArrayList<>());
        }
        res.get(curHeight).add(root.val);

        return curHeight + 1;
    }
}
// @lc code=end


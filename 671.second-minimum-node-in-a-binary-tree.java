/*
 * @lc app=leetcode id=671 lang=java
 *
 * [671] Second Minimum Node In a Binary Tree
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
    public int findSecondMinimumValue(TreeNode root) {
        if (root == null) {
            return -1;
        }

        return findMin(root, root.val);
    }

    private int findMin(TreeNode root, int min) {
        if (root == null) {
            return -1;
        }

        if (root.val > min) {
            return root.val;
        }

        int left = findMin(root.left, min);
        int right = findMin(root.right, min);

        if (left != -1 && right != -1) {
            return Math.min(left, right);
        }

        return left == -1 ? right : left;
    }
}
// @lc code=end


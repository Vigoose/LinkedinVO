/*
 * @lc app=leetcode id=101 lang=java
 *
 * [101] Symmetric Tree
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
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        } 
        return symmetricHelper(root, root.left, root.right);
    }


    private boolean symmetricHelper(TreeNode node, TreeNode left, TreeNode right) {
        if (node == null) {
            return true;
        }


        if (left != null && right != null) {
            return left.val == right.val;
        }

        return symmetricHelper(left, left.left, right.right) && symmetricHelper(right, left.right, right.left);




    }
}
// @lc code=end


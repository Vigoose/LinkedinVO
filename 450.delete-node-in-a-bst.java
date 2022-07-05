/*
 * @lc app=leetcode id=450 lang=java
 *
 * [450] Delete Node in a BST
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    public TreeNode deleteNode(TreeNode root, int target) {
        if (root == null) {
            return null;
        }
        // find the target node
        if (root.val > target) {
            root.left = deleteNode(root.left, target);
            return root;
        } 
        if (root.val < target) {
            root.right = deleteNode(root.right, target);
            return root;
        }
        if (root.left == null) {
            // case 1 & 2
            return root.right;
        } else if (root.right == null) {
            // case 3
            return root.left;
        }

        if (root.right.left == null) {
            // case 4.1
            root.right.left = root.left;
            return root.right;
        }
        // case 4.2
        TreeNode smallest = deleteSmallest(root.right);
        smallest.left = root.left;
        smallest.right = root.right;
        return smallest;
    }

    private TreeNode deleteSmallest(TreeNode root) {
        TreeNode pre = root;
        while (root.left != null) {
            pre = root;
            root = root.left;
        }
        pre.left = root.right;
        return root;
    }

}
// @lc code=end

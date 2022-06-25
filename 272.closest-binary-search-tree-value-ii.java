import java.util.Stack;

/*
 * @lc app=leetcode id=272 lang=java
 *
 * [272] Closest Binary Search Tree Value II
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
    public List<Integer> closestKValues(TreeNode root, double target, int k) {
        Stack<Integer> suc = new Stack<>();
        Stack<Integer> pre = new Stack<>();

        pushToSuc(root, suc, target);
        pushToPre(root, pre, target);

        List<Integer> res = new ArrayList<>();

        if (suc.isEmpty() && pre.isEmpty()) {
            return res;
        }

        while (k -- > 0) {
            if (suc.isEmpty()) {
                res.add(pre.pop());
            } else if (pre.isEmpty()) {
                res.add(suc.pop());
            } else {
                double sucHead = Math.abs(target - suc.peek());
                double preHead = Math.abs(target - pre.peek());
                if (sucHead < preHead) {
                    res.add(suc.pop());
                } else {
                    res.add(pre.pop());
                }
            }
        }
        return res;
    }


    private void pushToSuc(TreeNode root, Stack<Integer> suc, double target) {
        if (root == null) {
            return;
        }

        pushToSuc(root.left, suc, target);

        if (root.val > target) {
            return;
        }

        suc.push(root.val);
        pushToSuc(root.right, suc, target);
    }


    private void pushToPre(TreeNode root, Stack<Integer> pre, double target) {
        if (root == null) {
            return;
        }

        pushToSuc(root.right, pre, target);

        if (root.val <= target) {
            return;
        }

        pre.push(root.val);
        pushToSuc(root.left, pre, target);
    }
}
// @lc code=end


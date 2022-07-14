import java.util.*;

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
        List<Integer> result = new ArrayList<>();
        Deque<TreeNode> smaller = new ArrayDeque<>();
        Deque<TreeNode> bigger = new ArrayDeque<>();
        pushToSmaller(smaller, root, target);
        pushToBigger(bigger, root, target);

        while (k -- > 0) {
            if (smaller.isEmpty() || !bigger.isEmpty() && target - smaller.peekLast().val > bigger.peekLast().val - target) {
                TreeNode cur = bigger.pollLast();
                result.add(cur.val);
                pushToBigger(bigger, cur.right, target);
            } else {
                TreeNode cur = smaller.pollLast();
                result.add(cur.val);
                pushToSmaller(smaller, cur.left, target);
            }
        }
        
        return result;
    }

    /**
     * smaller: [2]
     * bigger:  [4,3]
     * 
     * 
     * @param smaller 
     * @param root
     * @param target
     */
    
    
    private void pushToSmaller(Deque<TreeNode> smaller, TreeNode root, double target) {
        while (root != null) {
            if (root.val <= target) {
                smaller.offerLast(root);
                root = root.right;
            } else {
                root = root.left;
            }
        }
    }
    
    private void pushToBigger(Deque<TreeNode> bigger, TreeNode root, double target) {
        while (root != null) {
            if (root.val > target) {
                bigger.offerLast(root);
                root = root.left;
            } else {
                root = root.right;
            }
        }
    }
}
// @lc code=end


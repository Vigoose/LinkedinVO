import java.util.*;

/*
 * @lc app=leetcode id=449 lang=java
 *
 * [449] Serialize and Deserialize BST
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        buildString(sb, root);
        return sb.toString();
    }

    private void buildString(StringBuilder sb, TreeNode root) {
        if (root == null) return;
        sb.append(root.val);
        sb.append(",");
        buildString(sb, root.left);
        buildString(sb, root.right);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data == null || data.equals("")) return null;
        Queue<String> queue = new LinkedList<>(Arrays.asList(data.split(",")));
        return buildTree(queue, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    private TreeNode buildTree(Queue<String> queue, int min, int max) {
        if (queue.isEmpty()) return null;
        String curNode = queue.peek();
        int val = Integer.valueOf(curNode);
        if (val < min || val > max) return null;
        queue.poll();
        TreeNode node = new TreeNode(val);
        node.left = buildTree(queue, min, val);
        node.right = buildTree(queue, val, max);

        return node;


    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// String tree = ser.serialize(root);
// TreeNode ans = deser.deserialize(tree);
// return ans;
// @lc code=end


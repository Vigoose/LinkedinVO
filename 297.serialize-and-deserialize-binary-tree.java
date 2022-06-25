import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;

/*
 * @lc app=leetcode id=297 lang=java
 *
 * [297] Serialize and Deserialize Binary Tree
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
    String splitter = ",";
    String NullNode = "#";
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        buildString(root, sb);
        return sb.toString();
    }

    private void buildString(TreeNode node, StringBuilder sb) {
        if (node == null) {
            sb.append(NullNode).append(splitter);
            return;
        }

        sb.append(node.val).append(splitter);
        buildString(node.left, sb);
        buildString(node.right, sb);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data == null || data.equals("")) {
            return null;
        }

        Deque<String> deque = new LinkedList<>(Arrays.asList(data.split(splitter)));
        return buildTree(deque);
    }

    private TreeNode buildTree(Deque<String> data) {
        String nodeString = data.poll();
        if (nodeString.equals(NullNode)) {
            return null;
        }

        TreeNode node = new TreeNode(Integer.valueOf(nodeString));
        node.left = buildTree(data);
        node.right = buildTree(data);

        return node;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));
// @lc code=end


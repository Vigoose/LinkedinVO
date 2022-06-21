import java.util.HashSet;

/*
 * @lc app=leetcode id=1650 lang=java
 *
 * [1650] Lowest Common Ancestor of a Binary Tree III
 */

// @lc code=start
/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
};
*/

class Solution {
    public Node lowestCommonAncestor(Node p, Node q) {
        HashSet<Node> set = getAllParent(p);
        while (q != null) {
            if (set.contains(q)) {
                return q;
            }
            q = q.parent;
        }

        return null;
    }

    private HashSet<Node> getAllParent(Node p) {
        HashSet<Node> set = new HashSet<>();
        while (p != null) {
            set.add(p);
            p = p.parent;
        }

        return set;
    }
}
// @lc code=end


/*
 * @lc app=leetcode id=323 lang=java
 *
 * [323] Number of Connected Components in an Undirected Graph
 */

// @lc code=start
class Solution {

    public int countComponents(int n, int[][] edges) {
        int[] parent = new int[n];

        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        for (int[] edge : edges) {
            int a = edge[0];
            int b = edge[1];

            int aParent = find(a, parent);
            int bParent = find(b, parent);

            if (aParent != bParent) {
                n--;
                parent[aParent] = bParent;
            }
        }
        return n;
    }


    public int find(int a, int[] parent) {
        if (parent[a] == a) {
            return a;
        }

        return parent[a] = find(parent[a], parent);
    }
}
// @lc code=end


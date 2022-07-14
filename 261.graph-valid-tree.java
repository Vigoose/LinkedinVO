import java.util.*;

/*
 * @lc app=leetcode id=261 lang=java
 *
 * [261] Graph Valid Tree
 */

// @lc code=start
class Solution {
    public boolean validTree(int n, int[][] edges) {
        UnionFind uf = new UnionFind(n);
        for (int[] edge : edges) {
            if (!uf.union(edge[0], edge[1])) {
                return false;
            }
        }

        return uf.size == 1;
    }

    class UnionFind {
        int[] parent;
        int[] degree;
        int size;

        public UnionFind(int n) {
            parent = new int[n];
            degree = new int[n];
            size = n;

            for (int i = 0; i < n; i++) {
                parent[i] = i;
                degree[i] = 1;
            }
        }

        public int find(int i) {
            while (i != parent[i]) {
                parent[i] = parent[parent[i]]; // path compression
                i = parent[i];
            }
            return i;
        }

        public boolean union(int a, int b) {
            int aParent = find(a);
            int bParent = find(b);

            if (aParent == bParent)
                return false;

            if (degree[aParent] < degree[bParent]) {
                parent[aParent] = bParent;
                degree[bParent] += degree[aParent];
            } else {
                parent[bParent] = aParent;
                degree[aParent] += degree[bParent];
            }

            size--;
            return true;
        }
    }

}
// @lc code=end

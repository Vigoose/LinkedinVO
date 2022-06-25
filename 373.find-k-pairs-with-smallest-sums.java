import java.util.ArrayList;
import java.util.PriorityQueue;

/*
 * @lc app=leetcode id=373 lang=java
 *
 * [373] Find K Pairs with Smallest Sums
 */

// @lc code=start
class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        List<List<Integer>> result = new ArrayList<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> (a[0] + a[1]) - (b[0] + b[1]));

        for (int i = 0; i < nums1.length; i++) {
            pq.offer(new int[]{nums1[i], nums2[0], 0});
        }

        while (k -- > 0 && !pq.isEmpty()) {
            int[] cur = pq.poll();

            List<Integer> list = new ArrayList<>();
            list.add(cur[0]);
            list.add(cur[1]);
            result.add(list);

            if (cur[2] < nums2.length - 1) {
                pq.offer(new int[]{cur[0], nums2[cur[2] + 1], cur[2] + 1});
            }
        }

        return result;
    }
}
// @lc code=end


/*
 * @lc app=leetcode id=76 lang=java
 *
 * [76] Minimum Window Substring
 * 
 *      0123456789
 * s = "ADOBECODEBANC", 
 *           j
 *      i
 * 
 * 
 * count[a] = 1
 * count[b] = 0
 * count[c] = 0
 * count[d] = -1
 * count[o] = -1
 * count[e] = -1
 * 
 * 
 * len = 1
 * maxLen = 6
 * t = "ABC"
 */

// @lc code=start
class Solution {
    public String minWindow(String s, String t) {
        int maxLen = Integer.MAX_VALUE;
        int strStart = 0;
        int start = 0;
        int end = 0;
        int[] count = new int[256];
        int len = t.length();
        for (char ch : t.toCharArray()) {
            count[ch]++;
        }

        while (end < s.length()) {
            count[s.charAt(end)]--;
            if (count[s.charAt(end)] >= 0) {
                len--;
            }

            while (len == 0) {
                if (end - start + 1 < maxLen) {
                    maxLen = end - start + 1;
                    strStart = start;
                }
                count[s.charAt(start)]++;
                if (count[s.charAt(start)] > 0) {
                    len++;
                }
                start++;
            }
            end++;
        }

        return maxLen == Integer.MAX_VALUE ? "" : s.substring(strStart, strStart + maxLen);
    }
}
// @lc code=end


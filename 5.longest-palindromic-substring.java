/*
 * @lc app=leetcode id=5 lang=java
 *
 * [5] Longest Palindromic Substring
 */

// @lc code=start
class Solution {
    /**
     * LC舞，不知道为啥阿三小姐姐一开始还问我能不能用trietree做这道题，
     * 对extendString那种beat90%的解法一开始不是很满意，
     * 虽然最后我还是按extend那种写了。
     * @param s
     * @return
     * 
     */
    int low = 0;
    int len = 0;
    public String longestPalindrome(String s) {
        if (s.length() < 2) {
            return s;
        }

        for (int i = 0; i < s.length() - 1; i++) {
            extendPalindrome(s, i, i);
            extendPalindrome(s, i, i + 1);
        }

        return s.substring(low, low + len);
    }

    private void extendPalindrome(String s, int start, int end) {
        while (start >= 0 && end < s.length() && s.charAt(start) == s.charAt(end)) {
            start--;
            end++;
        }

        if (end - start - 1 > len) {
            low = start + 1;
            len = end - start - 1;
        }
    }
}
// @lc code=end


/*
 * @lc app=leetcode id=245 lang=java
 *
 * [245] Shortest Word Distance III
 */

// @lc code=start
class Solution {
    public int shortestWordDistance(String[] words, String word1, String word2) {
        int index = -1;
        int min = words.length;
        for (int i = 0; i < words.length; i++) {
            if (words[i].equals(word1) || words[i].equals(word2)) {
                if (index != -1 && (word1.equals(word2) || !words[index].equals(words[i]))) {
                    min = Math.min(i - index, min);
                }
                index = i;
            }
        }
        return min;
    }
}
// @lc code=end


import java.util.*;

/*
 * @lc app=leetcode id=127 lang=java
 *
 * [127] Word Ladder
 */

// @lc code=start
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        HashSet<String> set = new HashSet<>(wordList);
        Queue<String> queue = new LinkedList<>();
        HashSet<String> visited = new HashSet<>();

        queue.offer(beginWord);
        visited.add(beginWord);

        int step = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();
            step++;
            for (int i = 0; i < size; i++) {
                String word = queue.poll();
                if (word.equals(endWord)) {
                    return step;
                }
                for (String nei : getNeighours(word, set)) {
                    if (visited.contains(nei)) {
                        continue;
                    }
                    visited.add(nei);
                    queue.offer(nei);
                }
            }
        }
        return 0;
    }


    private List<String> getNeighours(String str, HashSet<String> set) {
        List<String> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            sb = new StringBuilder();
            for (char c = 'a'; c <= 'z'; c++) {
                if (c == ch) continue;
                String newStr = str.substring(0, i) + c + str.substring(i + 1);
                if (set.contains(newStr)) result.add(newStr);
            }
        }

        return result;
    }
}
// @lc code=end


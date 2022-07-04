import java.util.*;

/*
 * @lc app=leetcode id=833 lang=java
 *
 * [833] Find And Replace in String
 */

// @lc code=start
class Solution {
    public String findReplaceString(String s, int[] indices, String[] sources, String[] targets) {
        List<int[]> indexList = new LinkedList<>();
        for (int i = 0; i < indices.length; i++) {
            indexList.add(new int[]{indices[i], i});
        }

        Collections.sort(indexList, (a,b) -> (a[0] - b[0]));
        StringBuilder sb = new StringBuilder();
        int start = 0;
        for (int[] indexes : indexList) {
            int sourceIndex = indexes[1];
            int index = indexes[0];
            if (s.substring(index).indexOf(sources[sourceIndex]) == 0) {
                sb.append(s.substring(start, index));
                sb.append(targets[sourceIndex]);
                start = index + sources[sourceIndex].length();
            }
        }

        if (start != s.length()) {
            sb.append(s.substring(start));
        }

        return sb.toString();





    }
}
// @lc code=end


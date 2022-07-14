import java.util.*;

/*
 * @lc app=leetcode id=244 lang=java
 *
 * [244] Shortest Word Distance II
 */

// @lc code=start
class WordDistance {
    int size = 0;
    List<String> strs;
    HashMap<String, List<Integer>> map;

    public WordDistance(String[] wordsDict) {
        map = new HashMap<>();
        strs = new ArrayList<>();
        for (String str : wordsDict) {
            if (!map.containsKey(str)) {
                map.put(str, new ArrayList<>());
            }
            map.get(str).add(size);
            size++;
        }
    }

    public int shortest(String word1, String word2) {
        List<Integer> list1 = map.get(word1);
        List<Integer> list2 = map.get(word2);
        int ret = Integer.MAX_VALUE;
        for (int i = 0, j = 0; i < list1.size() && j < list2.size();) {
            int index1 = list1.get(i), index2 = list2.get(j);
            if (index1 < index2) {
                ret = Math.min(ret, index2 - index1);
                i++;
            } else {
                ret = Math.min(ret, index1 - index2);
                j++;
            }
        }
        return ret;

    }
}

/**
 * Your WordDistance object will be instantiated and called as such:
 * WordDistance obj = new WordDistance(wordsDict);
 * int param_1 = obj.shortest(word1,word2);
 */
// @lc code=end

import java.util.*;
import java.util.HashMap;

/*
 * @lc app=leetcode id=380 lang=java
 *
 * [380] Insert Delete GetRandom O(1)
 */

// @lc code=start
class RandomizedSet {
    List<Integer> list;
    HashMap<Integer, Integer> indexMap;
    Random rd;

    public RandomizedSet() {
        list = new ArrayList<>();
        indexMap = new HashMap<>();
        rd = new Random();
    }

    public boolean insert(int val) {
        if (indexMap.containsKey(val)) {
            return false;
        }

        indexMap.put(val, list.size());
        list.add(val);
        return true;
    }
    
    public boolean remove(int val) {
        if (!indexMap.containsKey(val)) {
            return false;
        }

        int index = indexMap.get(val);
        int LastVal = list.get(list.size() - 1);
        indexMap.put(LastVal, index);
        list.set(index, LastVal);
        list.remove(list.size() - 1);
        indexMap.remove(val);
        return true;
    }
    
    public int getRandom() {
        return list.get(rd.nextInt(list.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
// @lc code=end


import java.util.*;

/*
 * @lc app=leetcode id=381 lang=java
 *
 * [381] Insert Delete GetRandom O(1) - Duplicates allowed
 */

// @lc code=start
class RandomizedCollection {

    List<Integer> list;
    HashMap<Integer, Set<Integer>> indexMap;
    Random rd;

    public RandomizedCollection() {
        list = new ArrayList<>();
        indexMap = new HashMap<>();
        rd = new Random();
    }

    public boolean insert(int val) {
        if (indexMap.containsKey(val)) {
            indexMap.get(val).add(list.size());
            list.add(val);
            return false;
        }
        Set<Integer> indexList = new HashSet();
        indexList.add(list.size());

        indexMap.put(val, indexList);
        list.add(val);
        return true;
    }

    public boolean remove(int val) {
        if (!indexMap.containsKey(val)) {
            return false;
        }

        Set<Integer> indexSet = indexMap.get(val);
        int index = indexSet.iterator().next();
        indexSet.remove(index);
        if (indexSet.isEmpty()) {
            indexMap.remove(val);
        }

        if (index != list.size() - 1) {
            int LastVal = list.get(list.size() - 1);
            Set<Integer> lastIndexSet = indexMap.get(LastVal);
            lastIndexSet.remove(list.size() - 1);
            lastIndexSet.add(index);
            list.set(index, LastVal);
        }
        list.remove(list.size() - 1);
        
        return true;
    }
    
    public int getRandom() {
        return list.get(rd.nextInt(list.size()));
    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = new RandomizedCollection();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
// @lc code=end


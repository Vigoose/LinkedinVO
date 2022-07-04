import java.util.*;

/*
 * @lc app=leetcode id=432 lang=java
 *
 * [432] All O`one Data Structure
 * 
 * https://leetcode.com/problems/all-oone-data-structure/discuss/91383/An-accepted-JAVA-solution-detailed-explanation.
 */

// @lc code=start
class AllOne {

    class ListNode {
        int count;
        Set<String> keySet;

        ListNode next;
        ListNode prev;

        public ListNode(int count) {
            this.count = count;
            keySet = new HashSet<>();
        }
    }

    ListNode head;
    ListNode tail;

    Map<String, ListNode> map;

    public AllOne() {
        head = new ListNode(Integer.MIN_VALUE);
        tail = new ListNode(Integer.MAX_VALUE);
        head.next = tail;
        tail.prev = head;
        map = new HashMap<>();
    }
    
    public void inc(String key) {
        if (map.containsKey(key)) {
            ListNode node = map.get(key);
            if (node.count + 1 == node.next.count) {
                node.next.keySet.add(key);
                map.put(key, node.next);
            } else {
                ListNode newNode = new ListNode(node.count + 1);
                newNode.keySet.add(key);
                addAfterNode(newNode, node);
                map.put(key, newNode);
            }
            removeKeyFromNode(key, node);
        } else {
            if (head.next.count == 1) {
                head.next.keySet.add(key);
                map.put(key, head.next);
            } else {
                ListNode newNode = new ListNode(1);
                newNode.keySet.add(key);
                addAfterNode(newNode, head);
                map.put(key, newNode);
            }
        }
    }

    private void removeNode(ListNode node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void addAfterNode(ListNode node, ListNode prev) {
        ListNode next = prev.next;
        node.prev = prev;
        prev.next = node;
        node.next = next;
        next.prev = node;
    }

    /**
     * Map<Integer, ListNode> countMap;
     * Map<String, Integer> keyFrequentMap;
     * @param key
     */
    
    public void dec(String key) {
        if (!map.containsKey(key)) {
            return;
        }

        ListNode node = map.get(key);

        if (node.count - 1 == node.prev.count) {
            node.prev.keySet.add(key);
            map.put(key, node.prev);
        } else if (node.count == 1) {
            map.remove(key);
        } else {
            ListNode newNode = new ListNode(node.count - 1);
            newNode.keySet.add(key);
            addAfterNode(newNode, node.prev);
            map.put(key, newNode);
        }

        removeKeyFromNode(key, node);
    }
    
    public String getMaxKey() {
        if (tail.prev == head) {
            return "";
        }

        return tail.prev.keySet.isEmpty() ? "" : tail.prev.keySet.iterator().next();
    }

    private void removeKeyFromNode(String key, ListNode node) {
        node.keySet.remove(key);
        if (node.keySet.isEmpty()) {
            removeNode(node);
        }
    }
    
    public String getMinKey() {
        if (head.next == tail) {
            return "";
        }

        return head.next.keySet.isEmpty() ? "" : head.next.keySet.iterator().next();
    }

    public static void main(String[] args) {
        AllOne obj = new AllOne();
        obj.inc("a");
        obj.inc("b");
        obj.inc("b");
        obj.inc("c");
        obj.inc("c");
        obj.inc("c");
        obj.dec("b");
        obj.dec("b");
        obj.dec("a");
        String param_3 = obj.getMaxKey();
        String param_4 = obj.getMinKey();
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne obj = new AllOne();
 * obj.inc(key);
 * obj.dec(key);
 * String param_3 = obj.getMaxKey();
 * String param_4 = obj.getMinKey();
 */
// @lc code=end


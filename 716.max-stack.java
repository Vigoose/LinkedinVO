import java.util.*;

/*
 * @lc app=leetcode id=716 lang=java
 *
 * [716] Max Stack
 */

// @lc code=start
class MaxStack {

    class ListNode {
        ListNode prev, next;
        int val;

        public ListNode(int val) {
            this.val = val;
        }
    }

    ListNode head, tail;
    TreeMap<Integer, LinkedList<ListNode>> map;

    public MaxStack() {
        head = new ListNode(0);
        tail = new ListNode(0);
        head.next = tail;
        tail.prev = head;
        map = new TreeMap<>();

    }
    
    public void push(int x) {
        ListNode node = new ListNode(x);
        ListNode next = head.next;
        node.next = next;
        node.prev = head;
        head.next = node;
        next.prev = node;

        map.computeIfAbsent(x, k -> new LinkedList<>()).add(node);
    }

    public int pop() {
        ListNode node = head.next;
        if (head.next == tail) {
            return 0;
        }
        removeNode(node);
        int result = node.val;
        map.get(result).removeLast();
        if (map.get(result).isEmpty()) {
            map.remove(result);
        }
        return result;
    }

    private void removeNode(ListNode node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    public boolean isEmpty() {
        return head.next == tail;
    }
    
    public int top() {
        if (isEmpty()) {
            return 0;
        }
        return head.next.val;
    }
    
    public int peekMax() {
        return map.lastKey();
    }
    
    public int popMax() {
        int max = peekMax();
        ListNode node = map.get(max).removeLast();
        removeNode(node);
        if (map.get(max).isEmpty()) {
            map.remove(max);
        }
        return max;
    }
}

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack obj = new MaxStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.peekMax();
 * int param_5 = obj.popMax();
 */
// @lc code=end


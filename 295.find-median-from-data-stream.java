import java.util.PriorityQueue;

/*
 * @lc app=leetcode id=295 lang=java
 *
 * [295] Find Median from Data Stream
 */

// @lc code=start
class MedianFinder {

    PriorityQueue<Integer> botQueue;
    PriorityQueue<Integer> topQueue;


    public MedianFinder() {
        botQueue = new PriorityQueue<>((a,b) -> (b - a));
        topQueue = new PriorityQueue<>();
    }
    
    public void addNum(int num) {
        if (botQueue.isEmpty() && topQueue.isEmpty()) {
            botQueue.offer(num);
            return;
        }

        if (num > botQueue.peek()) {
            topQueue.offer(num);
        } else {
            botQueue.offer(num);
        }

        if (topQueue.size() > botQueue.size()) {
            botQueue.offer(topQueue.poll());
        } else if (topQueue.size() + 1 < botQueue.size()) {
            topQueue.offer(botQueue.poll());
        }
    }
    
    public double findMedian() {
        return (botQueue.size() == topQueue.size() ? (botQueue.peek() + topQueue.peek()) / 2.0 : botQueue.peek());
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
// @lc code=end


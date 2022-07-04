public class caculateInterval {
    public interface IntervalLinkedIn {
        /**
         * Adds an interval [from, to] into internal structure.
         *   insert intervals变形，设计一个Intervals class，
         * 要求支持addInterval(int from, int to)和getTotalLengh()，
         * 总长度是intervals merged之后的长度。
         * 我面试时候是用list存没交集的intervals，
         * 每次update‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌有交集的部分。面试官其实有问我有没有更优的，
         * 其实可以用treemap存<start, end>的pair，key是start，value是end，
         * 反正存的是没有交集的intervals。
         * 
         * followup是再实现一个removeRange(from, to)的api，
         * 反正就是现存的range如果和from，to有overlap，
         * 那就把overlap的那部分interval删掉
         * （一个interval如果只overlap一半，那就只remove那一半）。
         */
        void addInterval(int from, int to);

        /**
         * Returns a total length covered by intervals.
         *  If several intervals intersect, intersection should be counted only
         * once.
         *  Example:
         * 
         *   addInterval(3, 6)
         *  addInterval(8, 9)
         *  addInterval(1, 5)
         *  
         *  getTotalCoveredLength() -> 6
         *  i.e. [1,5] and [3,6] intersect and give a total covered interval [1,6]
         *  [1,6] and [8,9] don't intersect so total covered length is a sum for
         * both intervals, that is 6.
         *      *
         *      *                   _________
         *      *                                               ___
         *      *     ____________
         *      *
         *      * 0  1    2    3    4    5   6   7    8    9    10
         *      *
         *      
         */
        int getTotalCoveredLength();
    }
}

"""
第一轮manager 很常规的bq，还会复数我说的话，进行confirm
第二轮 project dive，自己在白板说自己现在做的项目，面试官提问题交流，像做presentation
第三轮 system design，设计calender
第四轮 壹零壹，秒了之后问我有没有什么没考虑到的，比如input 是只有一条的tree，类似ListNode，太长导致Stack Overflow，问的我云里雾里的，shadow的中国老哥也是一脸疑惑。
 三期三，但不是sum，而是 multiplication，
第五轮 刘三流，变形了，input 不是 id number， 而是string name，不仅要算exclusion还要算incl‍‍‍‌‌‌‍‍‌‍‌‌‌‌‌‍‍‍usion， inclusion的定义是直接拿endTime - startTime
第五轮补充，method input（String funcName, List<String>logs）,要求返回对应funcName 的exclusion和inclusion time


1. 第一题是 贰肆叁
第二题是变种 找包含三个词的最小距离，思路是sliding window，dict count当包含3个词的时候算一下最小

第二题应该是简化版的气流
# https://www.1point3acres.com/bbs/thread-878851-1-1.html
"""

"""
public class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) {
            return;
        }
        ListNode fast = head;
        ListNode mid = head;
        ListNode fakeHead = new ListNode(0);
        fakeHead.next = head;
        ListNode last = fakeHead;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            mid = mid.next;
            last = last.next;
        }
        last.next = null;
        ListNode pre = null;
        while (mid != null) {
            ListNode next = mid.next;
            mid.next = pre;
            pre = mid;
            mid = next;
        }
        ListNode mover = fakeHead;
        while (pre != null && head != null) {
            mover.next = head;
            head = head.next;
            mover = mover.next;
            mover.next = pre;
            pre = pre.next;
            mover = mover.next;
        }
        if (head != null) {
            mover.next = head;
        }
    }
}
"""

"""
1. Design Calendar
2. HM BQ
3. 过去的project
4. Coding Round1: 利口 耳三舞, 耳三遛。 剩下二十分钟做利口妻易遛, 虽然觉得题目有点多但还是在最后全部做完了。
5. Coding Round2: 利口 尔奇铒, 一开始用O(logn)做法然后改成用Ｏ(n), 
接著连续两个follow up在O(n)解法裡如何减少space和如果tree imbalance如何提前结束, 这轮面试官引导的满好的, 也都回答出来了。

# https://www.1point3acres.com/bbs/thread-878361-1-1.html

"""

"""
word shortest distance

public class WordDistance {
    HashMap<String, List<Integer>> map = new HashMap<>();
    public WordDistance(String[] words) {
        for (int i = 0; i < words.length; i++) {
            if (!map.containsKey(words[i])) {
                map.put(words[i], new ArrayList<>());
            }
            map.get(words[i]).add(i);
        }
    }

    public int shortest(String word1, String word2) {
        if (!map.containsKey(word1) && !map.containsKey(word2)) {
            return -1;
        }
        int dis = Integer.MAX_VALUE;
        List<Integer> list1 = map.get(word1);
        List<Integer> list2 = map.get(word2);
        int index1 = 0;
        int index2 = 0;
        while (index1 < list1.size() && index2 < list2.size()) {
            int poi1 = list1.get(index1);
            int poi2 = list2.get(index2);
            if (poi1 > poi2) {
                dis = Math.min(dis, poi1 - poi2);
                index2++;
            }
            else {
                dis = Math.min(dis, poi2 - poi1);
                index1++;
            }
        }
        return dis;
    }
}

public class Solution {
    // build a graph, and do bfs every time
    public double[] calcEquation(String[][] equations, double[] values, String[][] queries) {
        HashMap<String, HashMap<String, Double>> graph = new HashMap<>();
        for (String[] equation : equations) {
            graph.put(equation[0], new HashMap<String, Double>());
            graph.put(equation[1], new HashMap<String, Double>());
        }
        for (int i = 0; i < equations.length; i++) {
            String[] equation = equations[i];
            double value = values[i];
            graph.get(equation[0]).put(equation[1], value);
            graph.get(equation[1]).put(equation[0], 1.0 / value);
        }
        double[] result = new double[queries.length];
        for (int i = 0; i < queries.length; i++) {
            String[] query = queries[i];
            double temp = search(query[0], query[1], graph, new HashSet<String>(), 1.0);
            if (temp == 0.0) {
                result[i] = -1.0;
            }
            else {
                result[i] = temp;
            }
        }
        return result;
    }
    
    private double search(String cur, String end, HashMap<String, HashMap<String, Double>> graph, 
        Set<String> visited, double product) {
        if (!graph.containsKey(cur)) {
            return 0.0;
        }
        if (cur.equals(end)) {
            return product;
        }
        visited.add(cur);
        HashMap<String, Double> neighbors = graph.get(cur);
        for (String next : neighbors.keySet()) {
            if (visited.contains(next)) {
                continue;
            }
            product *= neighbors.get(next);
            double temp = search(next, end, graph, visited, product);
            if (temp != 0.0) {
                return temp;
            }
            product /= neighbors.get(next);
        }
        visited.remove(cur);
        return 0.0;
    }
}
"""

"""
// two stack to store the successor and predesuccessor
 // inorder traverse the tree to get those
public class Solution {
    public List<Integer> closestKValues(TreeNode root, double target, int k) {
        Stack<Integer> pre = new Stack<>();
        Stack<Integer> succ = new Stack<>();
        inorder(true, succ, target, root);
        inorder(false, pre, target, root);
        List<Integer> result = new ArrayList<>();
        while (k > 0) {
            if (pre.isEmpty()) {
                result.add(succ.pop());
            }
            else if (succ.isEmpty()) {
                result.add(pre.pop());
            }
            else if (Math.abs(pre.peek() - target) > Math.abs(succ.peek() - target)) {
                result.add(succ.pop());
            }
            else {
                result.add(pre.pop());
            }
            k--;
        }
        return result;
    }
    
    private void inorder(boolean reverse, Stack<Integer> stack, double target, TreeNode root) {
        if (root == null) {
            return;
        }
        inorder(reverse, stack, target, reverse ? root.right : root.left);
        if ((reverse && root.val < target) || (!reverse && root.val >= target)) {
            return;
        } 
        stack.push(root.val);
        inorder(reverse, stack, target, reverse ? root.left : root.right);
    }
}
"""

"""
3.
只问了一道题，最大栈。是tag高频。
我先说了普通解法。（2个stack）然后说还有更高效的解法，他说先实现简单的吧。 然后就实现了一下。
讨论完时间空间复杂度以后，他reviwe了一下 没有bug。但是没编译或者跑test。
然后我说还可以用treemap和double linkedlist。然后分享了一下思路，口述每一个function怎么实现，
时间空间复杂度是什么，如何从treemap里找到list n‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌ode，如何删除或者增加node，之类之类。全程问的非常非常细节。
聊完了以后他说非常好非常好，不用担心任何事。
不过暂时recruiter还没给feedback，希望能过。

# https://www.1point3acres.com/bbs/thread-878278-1-1.html


4.
cs基础：semphore vs mutex， thread vs process，binary semphore，when to use semphore/mutex

招工网infra track是会考多线程的，确实难一些，需要准备的多，包裹也相对大一些。
lca in binary search tree（node可能不在树里），天竺人还非让我白板画一下

BST 找LCA，参考
《LC 235》


# https://www.1point3acres.com/bbs/thread-880894-1-1.html

5.
1 找树的高度。2给一堆pair表示相连的点，再给俩点问是否相连
Linkedin VO:
Coding: Min window substring, Word Ladder
Coding: num of island, max stack
SD: 给一个document repository设计索引系统。 需要能够在合理的时间内搜索出'what documents have the words red and green, but not blue' 之类的答案。如何计算和存储词语的i‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌ndex？

# https://www.1point3acres.com/bbs/thread-880560-1-1.html

# <===HERE===>
6.
电面：max sum subarray, max product subarray

1. HM, 几乎都在聊我现在的工作； sd就是常考题前几个
2. coding: 而物流，二期二
3. 国人大哥自己出题，搜遍全网都找不到该题目，直接把我打进十八层地狱 （国人不是都看地里的吗？国人不是都只考tag题吗?) - 求大哥如果看到该帖以后对自己人好一点, 找工作真的很辛苦T_T
我每道tag题都刷了3遍以上，然而... 只好move on了
题目记得不全，如下：
# - 实现FilterIterator
# class FilterIterator {
#    Integer value;
#   //这里要自己加field
#    FilterIterator(Selector selector, int[] array) {
#   //自己initiate
#    }
#    hasNext() {
# //implement
#    }
#    getNext()  {
# //implement
#     }
# }
# - follow up实现deep Iterator, 题目没弄明白，高手们自己看吧
# class DeepIterator implements Iterator {
#   DeepInterator(Iterator<Data> root‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌)
#   Integer getNext()
#   boolean hasNext()
# }
# interface Data {
#   boolean isInteger();
#   Iterator<Data> getCollection();
#   还有一个api貌似是getElement() 记不得了；我到最后也没弄明白这个interface，塞...
# }
不知道需求是什么，看着像是lc伞四要

# https://www.1point3acres.com/bbs/thread-880526-1-1.html


7.
刚面完，今天的面试，早上9点半才收到schedule. 前一天联系recruiter也没有人回复。
coding1: 1. 一二七 2. 三九
sd：top k
project dive deep轮：讲一个自己的project
manager轮： bq 问了一个小 design： 设‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌计一个service  给用户的monthly subscription收费
coding2: 做题网 account merge。
# https://www.1point3acres.com/bbs/thread-880499-1-1.html


8.
力扣 刘妖妖

9.
System design： 设计malicious ip blocker
coding：比较多，基本上是tag题：
1. BST和普通二叉树的LCA
2. 找一个sorted list里target出现的range
3. 判断两个树是不是一样
4. nested list value sum
最后一个coding题感觉不是莉蔻原题，由于面试官口音和我这边网络的问题，我对这个题的requirement感到非常ambugious。
大概是要实现一个类，这个类主要有两个方法，一个是accept一个sample（范型类）。 另一个是getResult()。 需要返回一个大小为k的sample list， k是一开始这个类的构造器输入参数。
具体产生list的逻辑由于楼主渣渣的听力确实没太听清楚，面试官有比较重的口音然后网络也不太好。我感觉大概的意思，采样需要根据sample count distribution进行概率分布。比如a采样了2次，b采样了3次，我们在最后return的list中，b出现的概率应该是3/5。
我感觉自己并没有读懂这道题的requirem‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌ent，所以在解题过程中和面试官产生了很大的discrepancy。面完之后非常好奇这个题的requirement到底是啥，希望有大神或者面过这个题的人讲解，十分感谢！
# https://www.1point3acres.com/bbs/thread-879789-1-1.html


10.
RetainBestCache
# https://www.1point3acres.com/bbs/thread-875690-1-1.html


11.
1. Design Google Calendar
2. Coding 迩奇迩
3. Coding 遗留雾灵 + 手写hashmap
4. 过去的project
5. HM BQ
# https://www.1point3acres.com/bbs/thread-874950-1-1.html


12.
5分钟introduction开始出题了  面试官问了thread VS process啥区别？
问了合理三角形这道题  首先问的是返回任意一个三角形咋办 确实没见过这题目 
给了个二分的解法说时间复杂度不合格  面试官给了些提示 想出来个O(n)解法, 
然后写代码很容易就写出bug free。
然后一个followup 就是和力扣一样的题目(六妖妖) 想了半天没想出来 后来提示想出来了 但是面试时间已经耗完。最‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌后留时间问了个问题 飘过了。

# https://www.1point3acres.com/bbs/thread-874013-1-1.html


13.
小三哥看着很和蔼，但是出题很血腥，一上来就出了一个Valid Number, 利口柳屋。雾草店面就上hard，我都没做过这题，上来给我整蒙了，
不一样的是没有那个optional的条件就是e/E的那个，其他都是一样的，
“."这个Corner case第一次没有注意到，经提醒之后改正。

然后第二题利口流气药，有一个不一样的是，他特地强调了leaf node 的value是unique的，
原题没有这个，感觉这个条件没有什么用啊，可能就是guarantee有一个解？
 我写出来了，而且口头跑了一遍，但是解题的时候思路比较乱，讲的‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌不是很清楚，不知道小哥给不给过。
综合的来说就是如果你很想去这家，就刷tag题就完事儿了，tag题频率低的也要刷。哎，反正感觉不太好，算了，move on吧。
# https://www.1point3acres.com/bbs/thread-872726-1-1.html


14.
第一轮算法：
里扣 溜旧 （+ follow up）
         而无溜
第二轮 讲自己组做过的项目： 遇到一位人很好的国人大哥，在这里道声谢，全程都很好，
而且我当时说了很真实关于我想离开现在这个组的原因（后来想起来感觉是给自己挖了坑，如果要是遇到一些隔壁邻居的面试官，我感觉我会gg），面完之后，
大哥还和我分享了很多他的工作经历，这一轮我觉得自己稍微准备一下，能够清晰的表达交流应该是没什么太大的问题。
第二天：
第一轮 系统设计： Top K （是常考题）推荐大家可以去油管搜搜视频，大概了解一下。
这个top k 我看到地里很多人都被问过，但是感觉要看面试官想主要考你哪个点，会问的稍微细。
（我这一轮是两个面试官，有一个shadow的小姐姐，小姐姐人很好，一直都微笑在听我，其实我觉得我这轮有些紧张。）
第二轮算法：
里扣 儿物寺 （这一轮面试官小姐姐要share screen，虽然但是有点紧张，
但是题目不算难，所以过程还是比较顺利。最后小姐姐还鼓励我对我说希望你之后可以加入领英）。
# https://www.1point3acres.com/bbs/thread-871537-1-1.html

15.
第一轮design topk，设计很简单估计大家都会，面试官可能有不同的侧重点，
这个面试官没有说我们k可以任意取值，时间上也只取过去5分钟，1小时和1天，
但是要求达到99%的精确度（一般的我们可能认为fastpath那个不需要很精确，但这里不行），
然后一直在问要在什么粒度上aggregate，这轮感觉答的一般，但也不是很差
第二轮
design metrics system，和上一轮结构有相似之处，把 metrics的schama设计明白就好了，high level结构和上一轮类似
第三轮
吃饭，不计分
第四轮
craftmanship，主要是behavior第五轮
本以为上午两轮design完了，答的还凑合，应该稳了，结果这一轮又问了个底层的design，要做的差不多类似于一个存储，
有一个producer不断的往这个存储里写东西，有多个consumer不断在这个里面读取东西，然后这个存储超过多少GB之后，
就要把老的东西给删掉，然后要我来design这个存储，本以为是用LRU多线程那种解决，
结果告知我不是要问这个，整个面试过程就在问我底层memory里各个byte，
各个地址要存什么东西，果然是很infra的题，在面试过程中完全不会，一边试着答，一边不断的跟面试官说我真的没做过这么底层的东西，
有可能是这个面试官给了我一个fail，但是提出来可能只是我的技能不适合infra而已
第六轮
coding ,merge n sorted list， follow up是如果有五千万个list，怎么用多线程解决，这个‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌follow up感觉答的一般，
因为每一步都要一个线程的话相当于第一步就得两千五百万的线程，这个感觉太多了，
然后他问我那我觉得多少个线程是合理的，我也没有概念，
我说大概10000个吧，然后就是第一轮先用10000个线程合并，他不置可否，这一轮不太清楚怎么样
# https://www.1point3acres.com/bbs/thread-871413-1-1.html


16.
1. Craft: BQ 但是感觉比其他公司更tricky一些：比如，你怎么improve team efficiency, 如何接手一个比较tricky的项目等
2. HM：聊得挺好的。你喜欢什么样的management style? 你怎么确保你面试的candidate和你一样优秀？
3. Lunch：介绍一些自己的背景，了解公司文化，然后了解自己的兴趣。我觉得这一轮也是会计入考核结果的
4. coding 1：伞溜溜
5. system design：top k
6. coding 2:  叁爸零，起要留
总的感觉比较好。coding都做出来了。就是system design感觉有点卡，因为问的会比较细。希望能有好结果！
祝大家都能拿到自‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌己满意的offer！
# https://www.1point3acres.com/bbs/thread-871255-1-1.html

17.
coding第一题：
这题很奇怪，是一个毛子SDE 问的，要求非常vague，说设计一个json parser，我开始还以为是design，后面他说要写code。input就是一个Json object，
要求能够parse 这个Json，但是我问他output是什么format，他说这个随你，
你觉得什么data structure 能用来展示一个json就用那个。我想了半天，说用map吧。
他不置可否。但是这个Json input 可以nest 其他的object, input 例如：
# {  "name" :"tom",  "location" : "NYC",  "age" : "28",  "hobby" :["basketball", "football"],  "colleague" : [{    "name" :"tom",    "location" : "NYC",    "age" : "28",    "hobby" :["basketball", "football"],   },   {    "name" :"Tony",    "location" : "SF",    "age" : "21",    "hobby" :["basketball", "football"]   } ] }
我心想这个json 每个field 的value 可以是string， integer，object，我只会java，
实在没想到一个好的representation 方式，一个小时过去了，写了一点skeleton code，面完就知道没戏了。

Coding 第二题：
刷题网：  要留领 + 要二期 这两个是高频，都bug free 做了
System design：
一个老头面我，开始一句话就是：这轮好像是desgin，我没准备好题目，你等我5分钟，我现在找个题。 我听了一脸黑线。
后面他出了个设计 rate limiter system。感觉和这个老头交流不是很顺畅。感觉很一般。
BQ：
一个白人面的，常规问题。聊得还行
Craftsmanship:
这轮也是问问题，像BQ，但是主要focus 问怎么让code 更加testable，怎么让syst‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌em 更加scalable或者 stable。一个三哥问的，全程没表情，像机器一样问问题。我感觉也一般，主要这些问题都太high level，我平时也没仔细想过。

# https://www.1point3acres.com/bbs/thread-871218-1-1.html


18.
第一题 lc @)
给了optimal solution (space O (1))
题目里只有（）没有其他两个
第二题lc ##
太久不面试了面到后来脑血糖不足hhh
想出了用binary search, 找的时候要看sequence排列， 但是最后boundary有点mess up
不造解出1.5题能不能给过

# https://www.1point3acres.com/bbs/thread-870760-1-1.html


19.
给一个integer的数组（有正有负，可以有重复）和一个k， 问能不能找出k个subset使每个subset的sum都一样，array里的每个数都要用上且不能重复使用。 
只需要返回true/false。
当时想的是先求出整个array的sum，sum/k = subSum, 相当于问能不能找出k个subset，
每个subset的和都是subsum。‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌最后写brute force给自己写晕了。。
举个例子 array=[2,10,6,-2,8] k=3 返回true  [2,6] [10,-2] [8]


https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
这题应该是刘就把，优化挺难的
# https://www.1point3acres.com/bbs/thread-870424-1-1.html

11.
算法题目不难，都是原题，三吧凌，三吧幺，二期二，尔物流

design就更离谱了，是linkedin自己的service，是非常具体的那种的要求和需求，
不像其他的design，你可以按自己的方式来进行，他直接从他要的方向开始问，而且很明显他已经有自己的答案了，
除非你按他的说，不然很容易被question，因为你确实没有他了解那个系统，整个过程也很让人不适，态度很差，爱答不理的，这轮应该是no hire。
# https://www.1point3acres.com/bbs/thread-869511-1-1.html


12.
2/11 phone screen， 里扣两道tag题->种花， word distance2（follow up是如果不停的query，怎么样优化-> 用map存query结果）
2/14通知过
3/3 VO 六轮。。。
第一轮：聊天
第二轮：里扣 刘酒憋。  第二题没找到原题，大概是儿摆 + pq做
第三轮：吃饭，尬聊
第四轮：SD，auto complete 系统
第五‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌轮：聊天，讲自己以前的项目
第六轮：李抠 散骑伞，气溜

# https://www.1point3acres.com/bbs/thread-869150-1-1.html

13.
力扣file system那题
关键infrastructure的组还花了十几分钟来问一些网络只是的题，比如thread/process, virtual memory（这个没答上来），tcp udp

1. Concurrency programming： 这个没办法，必考 （多线程还是得看的，好多其他公司也会考的，除非不做backend），
Leetcode concurrency section好好写一写，不过貌似现场不需要compile
2. Design整体偏底层，比如会有monitoring system， MQ，KV storage这种infra design

# https://www.1point3acres.com/bbs/thread-868759-1-1.html

14.
第一个刷题网 耳衣舞
第二个题目就是常见的RetainBestCache


15.
1. SD. topk 最高频了吧，面前一定要多想想，比如怎么存数据，比如存1min, 1hour, 1day， 然后怎么找到5min的topk
2. Concurrency. DelayTaskScheduler. 虽然提前准备了，无奈自己菜，真的是死记硬背，平时根本没写过多线程。面试官不理解我的方法，估计挂了。
3. 吃饭轮。
4. coding  李扣撕伊柳， 而伞舞
5. HR bq
6.Data Structure. 给一个时间windows，然后写get add getAvg(), get的时候element 如果过期了，
返回null. 重点讨论怎么处理过期的数据，在哪里进行删除，后来延伸到多线程境况下怎么处理。答的不好，磕磕巴巴，一到多线程也啥也不‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌会。
7. coding 李扣而百，而令撕另
# https://www.1point3acres.com/bbs/thread-868745-1-1.html

16.
上来先聊了聊怎么rank post， 怎么插广告。
然后就是simulate biased dice， 最后问能不能用O（1）。 我就整了个list把 [1111,222222‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌, 3333...] 放进去， 然后再random出一个数。
然后没有然后了。  

# https://www.1point3acres.com/bbs/thread-868504-1-1.html

17.
系统设计面的top K
算法面的和这个帖子一样：https://www.1point3acres.com/bbs/thread-843152-1-1.html，没想出最优解，
我处理matrix状态的时候面试官也有疑问，最后没有解决分歧。
想吐槽的一点是Linkedin的coderpad没办法execute，如果提出了和面试官想法不一样的解法，需要很大的cost去证明。
我VO面的一轮算法就是这里：https://www.1point3acres.com/bbs/thread-197717-1-1.html 第二题，
我算getTotalCoverage用了sort+移动窗口。面试官也是没见过，非说我的方法不能处理duplicate，
dry run了两个test case才‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌解决分歧，导致我第二题没时间写完。

# https://www.1point3acres.com/bbs/thread-867912-1-1.html

18.
round 1:  DFS数component个数，有点像数岛，但是自己构建graph; Max stak 用double listnode 做
round 2:  和经理聊天，就讲项目和BQ
round 3: 系统设计，求top k 注意这里的 k 是变量，就是说用户可以拿top 任意个数，所以不同于之前计算top k就不能只计算存储top k。有没有大神说下大概最优方案是啥。我应该答得不好
round 4: 画图讲自己项目
round 5: 三姐给了两道hard 而起儿 和 尔旧物 但都常见

# https://www.1point3acres.com/bbs/thread-867244-1-1.html

19.
上来先面了个valid 括号
又来了个Shortest Word Distance
面了一道nested list depth, （答：dfs）followup是如果depth计算是反着来的怎么办（答：bfs）
# https://www.1point3acres.com/bbs/thread-867032-1-1.html

20.
上来先SD， malicious ip 那道题，问的还挺细，问到distributed cache, API gateway, consistent hashing等等
然后resume deep dive, 楼主画图还可以，用zoom drawboard，建议面试前提前熟悉下
然后面的 all o 1（说实话有点惊讶，这题应该是hard++，楼主一年经验考这么难也是。。
不过还好看过面经，这题细节颇多。。。）
休息
又面的那个paragraph断句的 都是tag里的题，楼主用python，有点尴尬的是用python里 //是整数除法（ex: 5//2 = 2)
但是面试小哥显然不怎么懂python只会js，问我为什么要在code里加comment....
(js里//是comment符号） 解释了一下算是蒙混过关 ：）

# https://www.1point3acres.com/bbs/thread-866995-1-1.html

21.
比如：什么是进程和线程，什么情况下开一个新进程/线程；
什么是Mutex和Semaphore，两者区别；什么时候用Mutex什么时候用Semaphore；
Final, Finalize和Finally的区别是啥；什么是Virtual Memory。
这些基本系统概念完全没准备，BBQ了。答得一塌糊涂。
算法题目出得不难，类似蠡口五六，合并区间，只不过给你在一个interfac‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌e，
里面有AddInterval()和GetCoverLength()，输出总的覆盖的区间长度，让你去实现。
# https://www.1point3acres.com/bbs/thread-866624-1-1.html


22.
1.Nested List Weight Sum 两题中简单的那题 我记得一题是bfs或dfs都行 
另外一题最好bfs 否则要用dfs找深度 有很简单的followup
2.Pow(x, n) 给了o(n) 然后又给了recursive的O(logn)
3.Closest Binary Search Tree Value II 直接给two stacks的做法 因为时间复杂度最优 
但最后面试官说二叉树not neccessarily complete 所以worst case并非O(logn) 
然后口述了O(n）的做法 我练的时候 是用个deque在inorder traversal的时候 
右边界找到后做early termination 告诉了他 
    另外也提到了直接flatten成ascending order后 先扫一遍找到closest number 再用two pointer/sliding window。
    蠡口的答案最后一步写的是sort 感觉有点蠢
4.Intersection of Two Linked Lists 口述了用hashset记录节点 画了个O(n+m) time O(1) 
space的图后 花了一分钟写好 都是我在drive conversation 面试官事先也没要求O(1) space
5.序列化和反序列化二叉树 binary tree版本应该比bst版本容易一点 告诉他preorder和bfs都行 
但我口误了说了inorder 虽然后来写的还是preorder 后来那哥们followup说为什么preorder不行 
他自己的reasoning其实是有问题的
6.Insert Delete GetRandom O(1) 稍微改了点api的description 没有explicitly说是不是有duplicate 写了无duplicate 然后draft code了有duplicat‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌e
7.超级高频的一两题system design中的一道 说实话去面的人肯定会去过一遍

# https://www.1point3acres.com/bbs/thread-865539-1-1.html


23.
1. 蠡口鄂石
2. retain best cache（注意不是LRU）
2-Follow up: 如果要改变每个key的ranking怎么办？答用s‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌orted container

可以理解成一个有序数组，每次插入新元素时会自动排序（插入时间是O(lgn)）
Java中叫treemap
# https://www.1point3acres.com/bbs/thread-865363-1-1.html


24.
第一题 饵丝舞
第二题 伞柳寺

25.
第二题 而丝丝

26.
电面介绍自己之后是两道题，一个是leetcode上 Nested list weight sum 那道，我做出来了。
但是第二道是一道cache设计题， 我以为是类似于leetcode上的cache题，做的跑偏了。
面完发现他是这样的, 这是题目链接：
感觉有点悬
电面介绍自己之后是两道题，一个是leetcode上 Nested list weight sum 那道，我做出来了。
但是第二道是一道cache设计题， 我以为是类似于leetcode上的cache题，做的跑偏了。
面完发现它不是, 这是题目是这样的， 网上有答案
"""

"""
public class RetainBestCache<K, T extends Rankable> {
int entriesToRetain;
HashMap<K, T> map = new HashMap<K,T>();
DataSource<K,T> ds;
/* Constructor with a data source (assumed to be slow) and a cache size */
public RetainBestCache(DataSource<K,T> ds, int entriesToRetain) {
//impliment here
}
/* Gets some data. If possible, retrieves it from cache to be fast. If the data is not cached,
* retrieves it from the data source. If the cache is full, attempt to cache the returned data,
* evicting the T with lowest rank among the ones that it has available
* If there is a tie, the cache may choose any T with lowest rank to evict.
*/
public T get(K key) {
//impliment here
}
/*
* For reference, here are the Rankable and DataSource interfaces.
* You do not need to implement them, and should not make assumptions
* about their ‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌implementations.
*/
public interface Rankable {
/**
* Returns the Rank of this object, using some algorithm and potentially
* the internal state of the Rankable.
*/
long getRank();
}
public interface DataSource<K, T extends Rankable> {
T get(K key);
}
"""
"""
面试官问了问follow up：
- What if we want to implment this in multi-threaded environment?
- What i‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌f the rank will drift with time?

# https://www.1point3acres.com/bbs/thread-864126-1-1.html

27.
经典高频题，RetainBestCache那道题，地里有答案。TreeMap和pq都能做。follow up问了你还知道那种cache机制。答 LRU，可能是我写的太快了。面试官：那我们LRU该怎么实现呢？MMP还好这题我刷了也就10遍，doubleListNode + hashmap走你。LRU思路被问的很细，用codepad d‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌raw mode给他画图讲的。  最后过了安排VO

# https://www.1point3acres.com/bbs/thread-863783-1-1.html


28.
里扣 妖耳舞溜
让面试‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌官赶紧再出一道题，面试官给了nest sum


29.
面的是离口 义务另
不同的是会丢exception， 且返回结果是Double

30.
1. 要领要
2. 巫师棋
# https://www.1point3acres.com/bbs/thread-862247-1-1.html

31.
abc男 +三姐: 两道median,abc男给的 
儿要母(用quickselect写得其实有点bug,忘了n - k), 
三姐给的 三流事(比较有趣的是,写了最优解但abc男不懂觉得是错的,还给解释了一遍,最优解真的不可能自己想出来)
VO:
1.三姐面+国女shadow(记不清):两道median,一道 散思,用自己的方法写了一遍,
用interviewer的方法写了一遍,花了比较多的时间(好像不仅时间复杂度要最优解,连code本身也要最优解).
第二道,数岛,要求不用extra space,没时间了飞速秒,三姐写Java看到Python的range(n)在那儿说是不是错了
2.扯淡round,一个神神叨叨的phd面工作project,全程伴随着他大量的自言自语
3.三姐面+国女shadow:SD, top  k,答得有点水
4.好像是三哥?面,国男shadow:先给 鹅吃梨,再给 鹅企鹅
# https://www.1point3acres.com/bbs/thread-862049-1-1.html

32.
刷题网tag下高频写kmeans，然后易二奇，午菱


33.
第一轮国人小哥两道算法
第一题 要动动
第二题药量乖
第二轮国人小姐姐
第一题幺爸
第二题 k的‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌variation
sd 是面经 calendar
# https://www.1point3acres.com/bbs/thread-861273-1-1.html

34.
BQ:
how to make team efficient without your appearencetell me about a time you made a design decision and how you made that.
tell me about a time you made improvement suggestion
CS:
differences between link-list and array list
differences between threads and process
differences between virtual memory and physical memory
differences between heap and stack
differences between cache update mechanism: write b‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌ack and write through
LC 起药六，要求最好的的complexity。讨论trade off

# https://www.1point3acres.com/bbs/thread-861158-1-1.html

35.
设计real time TopK:  https://www.1point3acres.com/bbs/thread-823737-1-1.html
设计 calendar：User可以创event邀请其他人,收到的人可以接受/拒绝, 在自己的calenda‍‍‌‌‌‌‍‌‌‌‌‌‌‌‍‍‍‍‌r可以看到自己创的和受邀请的event.
设计malicious ip/blacklist: https://www.1point3acres.com/bbs/thread-841667-1-1.html
设计messge queue： https://www.1point3acres.com/bbs/thread-812910-1-1.html
设计search document：两个API，load和search,  inverted index
设计公司权限系统：https://www.1point3acres.com/bbs/thread-813582-1-1.html
设计metrics aggregation and monitoring system https://www.youtube.com/watch?v=UEJ6xq4frEw
key-value store： https://www.1point3acres.com/bbs/thread-841026-1-1.html
设计Autocomplete System：https://www.1point3acres.com/bbs/thread-834306-1-1.html
rate limiter： https://www.1point3acres.com/bbs/thread-843111-1-1.html
User Map：  h‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌ttps://www.1point3acres.com/bbs/thread-823737-1-1.html

# https://www.1point3acres.com/bbs/thread-860606-1-1.html


36.
1. 多线程题，本来以为是系统设计，到头来像OOD， 要求改来改去，到最后也不知道烙印要的是什么。题是有很多job要处理
同一时间可能有很多jobs或者一样的job可能执行很多次，要你去写一个class 却handle各种cases，具体的要一个一个问，确认了开始写，又来改条件，改来改去没写完。
2. 午饭聊天，跟经理的经理干聊也没饭吃。（汗）
3. 经理BQ（亚麻来的经理，各种BQ），最后十五钟加auto deployment system design
4. 文件系统+键值存贮器
5. 利口二期二+三六六+树换成图
6.弃药留+丝丝就
‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌题都是tag里的不难，估计要挂就挂在1

# https://www.1point3acres.com/bbs/thread-860021-1-1.html

37.
刷题网 舞散
follow up 义务而
思路被要求从头讲到尾，面试官会一直跟你说的思路
我还以为要跑，结果也不用跑，面试官会自己想一想，觉得不对的地方会指出来，如果你觉得你写的是对就说服他
最后10分钟留给我问问题（没设阅读权限，求一波米）

# https://www.1point3acres.com/bbs/thread-860142-1-1.html


38.
第一题： 雾散
第二题： 那道 cache 的OOD。。。

# https://www.1point3acres.com/bbs/thread-859691-1-1.html

39.
只用口头跑test case
二领 - 只有小括号
‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌尔斯斯

# https://www.1point3acres.com/bbs/thread-859455-1-1.html


40.
Coding 1: Insert an interval into a list of intervals
Coding 2: paint houses (3 colors for n houses, no two neighbor get the same color, get the min costs)
Coding 3: implement Increment/Decrement/getMax/getMin frequency with O(1)
System Design: get top n exceptions/errors in the system
BQ: how do you push for making a change? how do you convince your teammates? ‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌how do you convince colleagues from other teams?
# https://www.1point3acres.com/bbs/thread-859341-1-1.html


41.
Coding 1: Rotate Linked List by n position
Coding 2: NestedInteger: result = sum(value * level)

# https://www.1point3acres.com/bbs/thread-859335-1-1.html


42.
VO 面经 （他家连续6轮 中间只留30分钟 可以吃午饭，跟其他家每轮都有break相比，简直太累了）
Craft 轮：白人大叔 各种挖你平时怎么工作，怎么测试，犯过什么错，怎么解决。。。 第二轮面试官都来了，还想继续问。。
代码轮 1:  项目挑战 + 二伞无 额外条件 node 可能不在树里面。（由于上一轮一直在想例子，没有break，这轮code没发挥好）
代码轮 2: 二期贰 （说了先遍历， 然后 普通排序方法，priority queue 方法，binary search 方法，quick select 方法 求 k cloest） 让实现 binary search 方法
Lunch 轮：随便聊 （不计分）
设计轮：文档索引
HM：硬撑着又各种套例子。。。
# https://www.1point3acres.com/bbs/thread-859327-1-1.html


43.
25分钟 贰〇 +
贰肆肆 （提醒记得检查edge case，input 为 空 会怎么样？口头检查测试case，不需要compile + run）

# https://www.1point3acres.com/bbs/thread-845023-1-1.html

44.
1. 算法：伞吧零 散吧一
2. 实现Delayed task scheduler
3. 吃饭 和国人老哥聊的很开心
4. 算法：儿乞二，面经灭火题。这轮面的比较脑壳疼 第一题我用c++vector做的，遇到距离target更近的元素就去掉vector中头部的元素,O(n) 复杂度。
这题都做完了shadow的面试官突然冒出来说vector的erase不是(1)操作所以时间复杂度不对，
我说换成任何O(1) remove的structure就行，dequeue或者list, 然后我也不知道为啥在c++ vector erase是否是o(1) 操作bb了许久... 
第二题，  lz在clearify题目的时候问expected output输出是什么，面试官说i dont know, you give me an example let me see. 题目不难，但是最后没写完
5 SD k-v pair
6 manager
一个多星期后recruiter给回电话，说面的那个组决定move on因为我的背景和他们做的东西不fit，不过除了一轮算法feedback一般其它都面的不错他会把我介绍给

app track的recruiter。今天新的recruiter给了电话，现在大致几个选择：
1. 有一个app组对我感兴趣，需要我加面算法和design，但应该不会给我senior（就因为我差仨月满三年？），risk是如果面的一般overall feedback可能会不好
2. 继续等，等到有hm愿意直接捞。风险是时间久，久到被recruiter遗忘
3. 有一个SRE的hm愿意直接捞，如果我有兴趣的话不用加‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌面直接和hm聊，一切顺利的话直接offer
LZ在蕉厂一路比较波折，最近有点burn out就挺想换个环境。对于SRE这个岗位具体工作内容是完全不了解，
如果真的去了去搞一堆完全不懂的东西只怕比现在更累. 想请各路懂行的同志提提建议和看法。
大概率会take risk选1，but最近挂经有点多..
# https://www.1point3acres.com/bbs/thread-877260-1-1.html

45.
中国老哥抬了一手，感恩。
都是地里的题：里扣尔斯肆，RetainBestCache，用treemap做的

# https://www.1point3acres.com/bbs/thread-877021-1-1.html

46.
coding是 生成一个随机数根据weights （利口高频）。follow-up 是如何生成 multiple random ‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌numbers。time & space complexity。
# https://www.1point3acres.com/bbs/thread-876337-1-1.html

47.
招工网经典
RetainBestCache
# https://www.1point3acres.com/bbs/thread-875690-1-1.html

48
1. Design Google Calendar
2. Coding 迩奇迩
3. Coding 遗留雾灵 + 手写hashmap
4. 过去的project
5. HM BQ

# https://www.1point3acres.com/bbs/thread-874950-1-1.html

49.
5分钟introduction开始出题了  面试官问了thread VS process啥区别？
问了合理三角形这道题  首先问的是返回任意一个三角形咋办 确实没见过这题目 给了个二分的解法说时间复杂度不合格  面试官给了些提示 想出来个O(n)解法, 
然后写代码很容易就写出bug free。
然后一个followup 就是和力扣一样的题目(六妖妖) 想了半天没想出来 后来提示想出来了 但是面试时间已经‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌耗完。最后留时间问了个问题 飘过了。

# https://www.1point3acres.com/bbs/thread-874013-1-1.html

50.
小三哥看着很和蔼，但是出题很血腥，一上来就出了一个Valid Number, 利口柳屋。雾草店面就上hard，我都没做过这题，上来给我整蒙了，不一样的是没有那个optional的条件就是e/E的那个，其他都是一样的，“."这个Corner case第一次没有注意到，经提醒之后改正"
然后第二题利口流气药，有一个不一样的是，他特地强调了leaf node 的value是unique的，原题没有这个，感觉这个条件没有什么用啊，可能就是guarantee有一个解？ 我写出来了，而且口头跑了一‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌遍，但是解题的时候思路比较乱，讲的不是很清楚，不知道小哥给不给过。

# https://www.1point3acres.com/bbs/thread-872726-1-1.html

51.
第一轮算法：
里扣 溜旧 （+ follow up）
         而无溜
第二轮 讲自己组做过的项目： 遇到一位人很好的国人大哥，在这里道声谢，全程都很好，而且我当时说了很真实关于我想离开现在这个组的原因（后来想起来感觉是给自己挖了坑，如果要是遇到一些隔壁邻居的面试官，我感觉我会gg），面完之后，大哥还和我分享了很多他的工作经历，这一轮我觉得自己稍微准备一下，能够清晰的表达交流应该是没什么太大的问题。
第二天：
第一轮 系统设计： Top K （是常考题）推荐大家可以去油管搜搜视频，大概了解一下。这个top k 我看到地里很多人都被问过，
但是感觉要看面试官想主要考你哪个点，会问的稍微细。（我这一轮是两个面试官，有一个shadow的小姐姐，小姐姐人很好，一直都微笑在听我，其实我觉得我这轮有些紧张。）
第二轮算法：
里扣 儿物寺 （这一轮面试官小姐姐要share screen，虽然但是有点紧张，但是题目不算难，所以过程还是比较顺利。最后小姐姐还鼓励我对我说希望你之后可以加入领英）。
总体感觉，面试官人都很好，没有遇到什么故意被黑被刁难之类的，除了系统设计觉得自己有点紧张，其他感觉都还不错。
题外话，地里有领英的小伙伴是在App track的么，请问你们组还有L3的headcount么？ Recuriter和我说不确定啥时候会有headcount，他估计得等到四月份新的季度开始。这几天也在‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌看其他帖子，感觉领英的headcount/team match是不是都特别慢，因为现在手上没有其他offer，而且一直很想体验湾区食堂天花板，所以很希望自己可以快点面完最后一轮HM，拿到offer。

# https://www.1point3acres.com/bbs/thread-871537-1-1.html


52.
都是高频
乐扣 儿凌
乐扣 伞流丝

53.
1. 利口 伞伞玖
2. 利口 伞留寺

第二问的时候我先讲了一下BFS和DFS (two pass)分别怎么做，然后小哥哥让优化DFS。我问是要one pass吗？他说不用，说是存中间量。
然后我就想复杂了，我以为是用variable存一些中间结果，结果他的意思就是简单粗暴用hashmap存<level, sum>而已，
最后再loop一遍map。小哥哥网络不好，听他说话断断续续的，也导致我后面不是很get到他的意思。anyway，随缘了。
# https://www.1point3acres.com/bbs/thread-857940-1-1.html


54.
第一道题 判断括号（）是不是match. 只验证（）.stack压入弹出return true或false就好的那道题
第二道题 给一个string list，比如[“fox”,"the”,"quick”,"fox”] , 求给定的两个string的最短距离, 最短距离按照index计算, 这道题binary search.  
你要用一个hashmap 先存string和index的关系, key是string value是对应的index list, 因为可能出现多次, 然后他问fox到quick的最短的距离, 第一个fox是0 quick是2 距离就是2‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌. 第二个fox index是3 跟quick的距离是1,比第一个fox短, 所以返回1. string不存在list里的话 返回-1 .
然后问follow up，follow up用双指针.

# https://www.1point3acres.com/bbs/thread-857879-1-1.html

55.
1. HM:
一些常规的问题比如challenge project/遇到问题怎么办/理想的mgr是什么。。
一些不常规的问题：
如果有十个team分别own一个platform的一个part，现在这个platform要做某种migration，你怎么organize这十个team完成这个任务以及一系列follow up问题 
eg: 需要什么资源/怎么保证按时完成/怎么prioritize 这十个team的tasks/
我被问的有点懵，像是一个leadership的问题但是实在是没什么经验，就按照自己的感觉说了一通。
2. SD:
Trending share frequency 要求是算5min/1h/1day内的
reqiurement跟这个更像：https://xunhuanfengliuxiang.gitb ... -hour-24-hours.html
用的俄罗斯小哥的方法
4. Tech Communication
给两个人讲之前的项目，画图讲清楚就行
5. Coding 1
力扣 舅气伞，尔气气
6. Coding 2
力扣 而奇而  （用dequeue的方法 不能用priorityqueue）
力扣 舅撕

# https://www.1point3acres.com/bbs/thread-857301-1-1.html


56.
lc 榴姨
lc 尔丝丝
看了近两个月的面筋，coding 一般都是lc面筋题，一道简单的一道稍微难一点的+followup
# https://www.1point3acres.com/bbs/thread-857295-1-1.html


57.
第三轮是系统设计第二轮 找朋友的的degree写代码。给你一个function，两个input，
你自己的id和另外一个user的id。然后在给一个api，find(id）然后返给你一个list of friends. 
要求找到degree3以内的，超过就算3.
解法，先看看第一个人的好友列表有没有另外一个人，如果没有就看双向拿好友list看看有没有重合。
迅速写完之后开始画图设计这个，怎么样scale，怎么样的数据库巴拉巴拉。
第三轮是系统设计第三轮，设计kv store。
# https://www.1point3acres.com/bbs/thread-856252-1-1.html

59.
1. 利口 儿时
2. 利口 雾散
3. 利口 易武耳

# https://www.1point3acres.com/bbs/thread-856085-1-1.html

60.
Host Manager轮：国人manager，GG六年，跳过来L养老，正常BQ，介绍team，
给了一个情景题：有个老的service很多bug，performance也不好，developer experience也很差，请问怎么修，etc。
Tech Communication: 国人staff面的，介绍自己的project，介绍明白了，
但可能tech stack真的差的有点多，没有产生共鸣，国人大哥挠了挠头，
事后还看了我linkedin两次，想加他可是没通过，GG。
System Design: 一个土耳其的白人小姐姐面的，她刚转成manager，
感觉她背景就是很简单的web dev，没啥system design的背景，所以面的很水，
问的是malicious ip那题，follow up我按面筋答没啥问题，提到了bloom filter她也不知道是什么，
我解释了一遍，她象征性的问了问怎么scale，我也简单答了一下，她可能确实不会distributed system，
就记了记我说的，拍了张照我的design就草草结束。。

Conding 1：国人大哥放水的题 伞巴陵 follow up 伞巴以
Coding 2：邻居大哥的难题 Find All Palindrome Subsequences，这真是挂人题，
我一直在往dp的O(n^2)的解法想，事后搜了一下发现最优解是O(n^3)，想了一小时都没做出来，
可能也是自己太菜了把。最优解请看这里：https://leetcode.com/disc‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌uss/int ... dromic-Subsequences

# https://www.1point3acres.com/bbs/thread-855036-1-1.html

61.
LZ在准备infra 面试，Concurrency方面的有三轮 concurrency，data&algorithm ， complex system. 刷了大部分面经后发现infra的data&algorithm这轮内容考的有点杂，有些面经提到这轮就是普通的算法题，有一些则是LC上的concurrency题目，剩下则是一道类似设计的题目，要求大概是
设计一个key-value store
1. create ‍‌‍‍‌‍‍‍‍‌‍‍‍‍‌‌‌‍a file
2. delete a file
3. ap‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌pend something to a file.
面经给出的细节不多..感觉是用SD的角度去做这道题，但如果是这样这一轮的归类不应该也是SD吗..想问问有过经验的道友这一轮这道题到底要从什么角度去解

# https://www.1point3acres.com/bbs/thread-854341-1-1.html

62.
第一轮序列反序列儿茶树。秒了测了半天，最后问我bst怎么优化没想出来，
结果竟然是按谦虚遍历可以省去分隔符。体验还不错
第二轮国人hm bq. 人不错感觉水平很高，是我面试以来唯一一个问我的project问题问到点儿上的。
第三轮设计日历，api和data model还没过完就被烙印追问workflow和design细节了大半个小时，
搞的最后没时间画出High level design。可能这里就挂了。
系统设计真的是千人千面，以后干脆问完requirement直接画high level design
第四轮题库两题, 一个easy太简单忘了另一个高频萨溜溜
第五轮tele comm彻底破防。一个白大爷，像国内某些面试官一样全程diss，
比如你讲了一通design 从无到有各种trade off最后决定用到了某种aws service，
他总结就一句：所以你做的just some configure是吗。
中间不断带跑话题到稀奇古怪的地方 (比如亚麻不像ebay那样是第三方卖家直接卖东西?)。
还在讲话过程中突然偏头看向一边走神几十秒，我不得不停下问他是有什么事？
回曰老婆出门了，他在想老婆为什么出门没告诉他原因。。。。 
总之我后面忍无可忍，顶了几句草草结束了，手里不是没其他offer非得受这个气。
最后问题问最喜欢公司的什么，老汉答曰公司文化好，不‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌干活就做做build and release, 
五十多岁就等退休了，反正不会开除他。
round1: 省去分隔符 -> 省去null

# https://www.1point3acres.com/bbs/thread-854334-1-1.html

63.
echnical 是一轮system design 2轮coding
system design: calendar app
coding:
第一轮:
1. reverse words in a sentence, constant space  follow up : 怎么处理多余的空格和标点符号
2. level order traversal in n-ary tree， 输出格式 “1 $ 2 3 4 $ 5 6” 就是每层用一个特殊符号隔开
这一轮的面试官感觉不是很上心， 两道题做完了就直接提前挂电话了
第二轮;
LC 730
本人水平有限 system design 完全bomb了，
 coding第二轮没想过遇到个lc hard 之前没做过 
 最后写了个递归的解法 follow up 1 ; 
 怎么把solution 变成iterator 就是 call 一次 然后给出下一个 palindrome， 
 没答出来， follow up 2: 怎么优化递归解法的space ， 这应该是提示要dp或者memo， 没答出来
bq 问的也比较仔细 建议熟悉一下简历 和‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌挑一个自己能熟练介绍的project

# https://www.1point3acres.com/bbs/thread-853765-1-1.html

64.
电面：
Question1: O(1) 实现 valid parenthese； 
Question2: 给一串string 的list，input是两个string，找两个string之间index的最小距离（string有可能重复出现）
VO：
Round1：Project deep dive， bq
Round2:  Design google books
Round3:  number of Islands 和 maxStack
Round4: Allforone 面经看到过但是我看它是hard就每次都略过...karma is 那啥‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌。反正是没做出来（摊手）
Round5: Manager round

# https://www.1point3acres.com/bbs/thread-853478-1-1.html

65.
刷题网 ：尔领
第二题：
刷题网： 尔斯斯

# https://www.1point3acres.com/bbs/thread-853446-1-1.html

66.
问了很多java 细节的东西：
CPU/GPU
Thread/process
transaction是什么，java的exception
virtual memory/paging, final/finally/finaliz‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌e
还有什么swap memory 之类的
code：
利口1零贰，
+ RetainBestCache

# https://www.1point3acres.com/bbs/thread-851687-1-1.html

67.
1. 类似于valid parentheses，但是只有括号。
2. 利特口德：巫伞
3. 利特口德：药物儿

昂塞特：
按脚coding：就是地里那道survey的题目，秒了
设计：设计news feed，面试官侧重问了安卓里面具体的实现。
DSA：思叁贰[/size‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌]
吹逼轮：各种聊，开心就好。

# https://www.1point3acres.com/bbs/thread-850983-1-1.html

68.
先聊聊天幾分钟, 然後問了一些Java基础八股文. 最後做題
高频问题
利口 山傘酒利口 兒零

# https://www.1point3acres.com/bbs/thread-849004-1-1.html

69.
刷题网 1. 利口 刷墙那道 2. 自己出的题目

merge k sorted list
# https://www.1point3acres.com/bbs/thread-848908-1-1.html

70.
一堆operation system的基础题，问了PAGE FAULT, TCP/UDP, SEMAPHORE
Coding 新题：
public abstract class pBuffer {
  protected final int BLOCK_SIZE = 1024;
  protected final int BLOCK_COUNT = 1024;
  /*
   * A sample 1mb buffer, to be allocated in 1k chunks.
   * Other sizes are definitely possible.
   * How do things change if it's a 1GB buffer?
   */
protected byte[] buffer = new byte[BLOCK_COUNT * BLOCK_SIZE];
  /*
    ____________________________________________
    |.0   |. 1  |.   |. |.  |. 5 |. 6|
    ____________________________________________
  */
  public pBuffer() {
    /*
     * Reads the buffer from file and dumps the contents into the array,
     * restoring the state to what it was when onShutdown() was called
     */
    fillBufferFromFile();
  }
  // Called on shutdown
  private void onShutdown() {
    /*
     * writes the full contents of the buffer to disk,
     * for reading when later invoked by the constructor
     */
    writeBufferToFile();
  }
  /// ---------------------------------------
  class Location {
    }
  }
   // Returns a Location for a free block of the buffer, suitable for passing to put, get, and free
  public abstract Location create() throws NoAvailableSpaceException;
   // Stores up to BLOCK_SIZE bytes of data in location l. Data beyond BLOCK_SIZE bytes should be truncated
  public abstract void put(Location l, byte[] data);
  // Returns the BLOCK_SIZE bytes of data stored at location l, or null if l is unallocated
  public abstrac‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌t byte[] get(Location l);
   // Indicates that an area of the buffer is no longer needed, and can be reused
  public abstract void free(Location l);
}


这题是不是和157 158有点类似，read4那个？
# https://www.1point3acres.com/bbs/thread-848735-1-1.html


71.
第一轮：
系统设计。Top K Shared Links，实时统计linkedin被转发次数最多的links，
类似于twitter trends，要求统计每5min，30min，1day的前20条links。
这就就按youtube有个视频答的，分fast path，slow path统计。
fast path用count min损失一些精确度来快速产生短时间段的统计数据，slow path就用常规MapReduce。
第二轮：
LC舞，不知道为啥阿三小姐姐一开始还问我能不能用trietree做这道题，
对extendString那种beat90%的解法一开始不是很满意，虽然最后我还是按extend那种写了。
LC起要留 原题。
第三轮：
tech arch轮，领英独有的画自已过去一个project的架构图讲给面试官听。
这个还是提前准备下好。
第四轮：
insert intervals变形，设计一个Intervals class，
要求支持addInterval(int from, int to)和getTotalLengh()，
总长度是intervals merged之后的长度。
我面试时候是用list存没交集的intervals，
每次update‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌有交集的部分。面试官其实有问我有没有更优的，
其实可以用treemap存<start, end>的pair，key是start，value是end，
反正存的是没有交集的intervals。
followup是再实现一个removeRange(from, to)的api，
反正就是现存的range如果和from，to有overlap，
那就把overlap的那部分interval删掉
（一个interval如果只overlap一半，那就只remove那一半）。
第五轮：
纯和HM聊天，问BQ。

# https://www.1point3acres.com/bbs/thread-848471-1-1.html

72
第一题：LC耳奇异  变体。string里面的char没有任何限制所有字符都有可能，所以不能用特殊符号分割。所以我是每个string encode成一个长度+原string，parse的时候先读取length，然后根据length读取原string。
第二题：L‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌C而齐齐 原题。

# https://www.1point3acres.com/bbs/thread-848449-1-1.html

73.
1，thread 和process的区别。2，什么是transaction。 3，mutex 和semaphore的区别。
然后coding就是RetainBestCache，写出来了。follow up不是thread safe，是LRU该如何实现。我说了用deque。磕磕巴巴。

# https://www.1point3acres.com/bbs/thread-848344-1-1.html

74.
一个小时的电面其中二十分钟behavior question，之后就是coding。
coding就是面经题目，算一个netsted的list的weighted sum要求的是reverse weight就是约底层嵌套越多weight越低，
最下层的weight是1依次递增。[[1, [2]], 3, [4]] = 1 * 2 + 2 * 1 + 3 * 3 + 4 * 2 = 21 这个样子。
我当时就是先用了dfs吧好像找了一下最大多少层，然后再用的bfs来把每一层的和算一下加起来。
之后问了问time/space‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌ complexity是多少，一共就花了二十分钟吧，最后我也没啥好问的于是提前十几分钟就结束了。

# https://www.1point3acres.com/bbs/thread-847718-1-1.html

75.
1: BQ，白人小姐姐EM，白人小哥SEM影子。两位EM都很nice，聊得也很开心，因为LZ工作年限很长，所以有不少故事可以分享。总体感觉很好。
2: 台湾小哥。先出了一道149，花了一点时间完成了，然后就聊了一会，后来小哥在44分以后说，
我再出一题，汗，只能再做一题，但是可能是时间太紧张了，后面一题没做出来。
我一开始的方法应该是对的，使用backtracking，小哥估计看见我没做出来也急了，
拼命给hit，然后我最后时刻，把backtracking又改掉了，然后就不对了。小哥后面和我说，那个backtracking的思路是对的，就差一点点了。

小哥还说，我也许不应该出第二题。事后我再看这题，也就是20分钟就做出来了。另外第二题不是做题网的题目。
3:白人老哥。设计一个feed的系统。LZ之在之前公司参与过很多个APP的系统设计，所以这一轮应该表现得很好。
4:国人小哥。本来以为是做题，后来发现是写一个小APP。刚开始LZ觉得这个不是很困难，绝对可以完成，结果实际一做，
发现需要搞定的细节太多了，时间太紧张了。国人小哥也很nice，还和我讲，这个小APP比之前他们的实操小APP要更难一点。
事后我和小哥讲，如果data那个格式整理得更好一点，时间应该来得及的。就是因为那个data存在2个列表里面，需要颠来倒去的转，所以要写很多相关代码。
# https://www.1point3acres.com/bbs/thread-846636-1-1.html

76.
1. 以前给team提过的建议 别人采纳了没
2. mentor过别人没
3. 有没有leading过project 也有问跟人合作的项目
coding是常见的RetainBestCache题，问了时间复杂度。问了为什么先看要不要evit再从ds取数据，
follow up问了如何thread safe，在哪里加锁。我对concurrency不是很了解 反正就是答了写入map的时候需要存。
后来小哥也有说从cache取得时候其实最好也加，不然其他process正好evit了 那你取出来的就是Null 所以可以null check一下你从cache拿到的数据。
然后我说我实际工作中concurrency用得确实不多，小哥就说 那thead safe就聊这些 我们看看其他的问题。不知道会不会有啥影响。
接着就问了如果ranking一直在变化怎么办，会不会改变自己的solution。 我就聊了LRU，用map+dll.

# https://www.1point3acres.com/bbs/thread-846598-1-1.html


77.
先问个问题：之前recruiter给我发的流程里有这个HM轮（所以总共5轮），但是只给我面了除HM以外的4轮，这是什么情况啊？
另外我看了我当时投的岗位的广告已经被撤下来了，这说明什么呢？有点慌啊。。。
第一轮 coding，流散流 变体，改成求某个特定function的结果，follow up问O(n)空间复杂度的做法
第二轮 coding，散期散，follow up问三个数组怎么办
第三轮 SD，calendar
第四轮 聊项目
更正：第1轮follow up要求是O(1)空间复杂度


# https://www.1point3acres.com/bbs/thread-845831-1-1.html

78.
第一道是括号题，老朋友了，蠡口二零，而且只问了我小括号，希望我给出O（1）的解法，其实就是count那个解。我其实第一时间也没有想到，先写了stack的。
第二题是幺饵捌，我当时看面经没看到过，确实也忘了最优解……是先讲了O（n^2）的，然后小哥提了sorting，再在第一种方法的基础上改成了O（n）的解法。

# https://www.1point3acres.com/bbs/thread-845812-1-1.html

79.
1 - Technical Interview问了我一道flattern的题目。(((1，3，4)，(2，1)，1)-> flattern成[1, 3, 4, 2, 1, 1]
有一个Collection Class里面有三个methods是bool isInteger，vector<Collection > getCollection，还有一个忘记了可能是是不是空之类的。
要求写constructor，next，hasNext；并且尽量linear的输出next。
所以我就在constructor里先flattern整个collection成一个vector，然后用private vector去储存它，next/hasNext就直接写就行。
Follow-up：
怎么样能缩短constructor的时间->把flattern逻辑写在next里面
体验一般，我用C++面试，他给我的是Java的题目，刚开始看我真的一脸蒙圈，但我最后问了小哥哥解释说Linkedin是一家大部分用Java的公司，除了Python题目有些会单独做其他不会。（但我还是觉得很不用心啊，太懵了）
2 - Technical Interview
这一轮两个面试官面我，简直是人间灾难。一个小哥哥说话murmuring，给我讲题目说了2分钟我大概只听到了一个词Tree，然后跟他说了他换了耳机就好了一丝丝，
后来再跟他说他再换了耳机好一些了但他说话就是那种喃喃自语的，真的很难听清楚。体验极差，
后面我都在cue流程 说就到这里吧（心里想的是放我走让我出去我受不了了）。而且两个interviewers，就很容易出现一个人没在听，大家不在same page的情况，很绝望。
两道题：
1. Tree找树的level， bottom-up的那种。
2. 做蛋糕，neighboring颜色不一样 e.g. 如下图最minimum cost是4dollars。考虑有N个蛋糕，但只有三种颜色
               cake1  cake2 cake3
red           1        2          100
yellow      100     100        1
blue         2         100        1
用一个length是3的vector存每个蛋糕当前颜色下的min cost。这应该是DP把？
Follow-up：
如果第一个cake 和最后一个蛋糕的颜色也要求不一样。我说那就存3x3的matrix记录第一个蛋糕不同的颜色。
3 - manager round   
一个小姐姐，问了项目，问了如果最近组里刚刚做完一个big migration，service load time increase让我修bug需要什么资源要怎么修。
（我答的应该不是很好，第一次面这种面试有点没有经验。面试官很nice很professional就是有一点点不好聊天让人有点紧张）
4 - system design
设计一个calendar like google calender 这轮是体验最好的一轮，面试官很nice有问必答，沟通也很顺畅。
5 - Technical Communication
讲一个自己参与的项目，让他听懂。从high-level design，问到了具体怎么存data大致的格式，有什么主要的endpoint。画了client server database的图。体验一般‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌般，到后面有种被逼问的感觉。
All in all，体验特别特别一般。特别是second round，我觉得哪怕我一点都不准备让我去面试别人也不会像那个小哥哥一样糟糕。
但我自己也有点问题，毕竟第一次面这种system design和technical communication这类的后面3/4/5轮，有点没经验导致的不自信。
（recruiter给我的feedback也是这么说的）Anyways祝大家接下来面试好运，遇到好的面试官！
还有一个信息，因为手里有offer我面试完就催了recruiter，她隔了一天就跟我说fail了，feedback很及时效率很高，挺professional的。

# https://www.1point3acres.com/bbs/thread-845337-1-1.html

80.
店面:
RetainBestCache. Follow-up: 如何保证thread-safe.
昂赛：
Coding1: 思伞尔,这一轮感觉面试官都妹懂我讲的2 map solution，然后最后要求强行用一个他会的方法解..也写出来了 (最后就挂在这轮)
Coding2: 易伞久 + 物流变形 邻国hxd
SD: 限流器
BQ: 常规
Craftsmanship: 问了问关于提升代码质量，带新人，带project相关问题
一些之前看别的帖子，看到的关于Craftsmanship的资料:
https://business.linkedin.com/co ... ok-8-7-17-uk-en.pdf
https://thenewstack.io/linkedin-code-review/

# https://www.1point3acres.com/bbs/thread-845196-1-1.html

81.
25分钟 贰〇 +
贰肆肆 （提醒记得检查edge case，input 为 空 会怎么样？口头检查测试case，不需要compile + run）

# https://www.1point3acres.com/bbs/thread-845023-1-1.html

82.
刷题网 伞柳寺，两种方法都要写
刷题网 尔寺寺 一开始以为是尔寺伞，讨论了一下发现问的是尔寺寺
# https://www.1point3acres.com/bbs/thread-844327-1-1.html

83.
发一个领英 senior sde 面经，面试的是湾区的 flagship 组的
我的面试官基本全是国人，发面经感觉有很大的几率被认出来。。。不过反正也挂了，无所谓了
1. BQ 轮 + Project Deep Dive，但是大部分时候是 manager 他在讲。。。最后感觉我就说了个 challenging project
2. 散酒 + 要死就，第二题输入的坐标有可能是 double。。争了半天没弄清楚，
按照面试官的意思强行写了个 HashMap 存 double 的斜率的方法。但是我觉得这方法至少在 java 里面还是跑不过的
3. TopK, realTime 获得最近 5 分钟, 1小时, 1天的 click 数目中的 topN。QPS很小所以扯那些大数据的处理方式都错了。
时间相关的 topK 没准备好，面得很差。面试官很 supportive，确实是我自己太菜了。。
4. 第一题散吧领，第二题而就其，做完还有很多时间，给了个 bonus followup 是思思就，优化是可以把转换成的 string 中的 null 给优化掉。面试官指导了很多，还是很有意思的算法。
只有 4 轮，好像是把 BQ 和 project dive 合在一起了。
领英的 HR 说是给面 senior，但是还是按 junior sde 安排的面试官，说如果你面试特别好的话我们会考虑把你 uplevel 到 senior。。这个 HR 真的各种不靠谱。
我这挂了一轮的肯定没啥机会了，就 move on 吧

# https://www.1point3acres.com/bbs/thread-843799-1-1.html

84.
最近面了邻英的staff，本来以为面试题库不大，应该会是面筋常见题，结果面试官出了个bestretaincache，有个capacity。 大
致意思就是有个kv store的cache，还有个getrank（），然后每次新数据来，先从cache里面取，如果cache没有，就从ds 数据库里面取，如果cache满了，evict rank最低的数据。 followup是如果来了rank更低的数据，如何直接不存cache里面。 然后下一个follow是如果rank是变化的怎么办。
题目一开始做出来了，后来面试官指出了getrank的一个小问题，数据得先存进去再从cache找rank更快，然后写的时候有一点磕碰。最后挂了‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌。 
遗憾，本来以为邻英会是个简单的，结果店面就挂了

简单说是马甲版 蠡口 撕留领
看起来是地里之前出现过的这题~ https://www.1point3acres.com/bbs/thread-484962-1-1.html
# https://www.1point3acres.com/bbs/thread-843719-1-1.html

85.
蠡口 腰屋要
follow up1： 前面有空格
follow up2： 前面和后面都有空格

# https://www.1point3acres.com/bbs/thread-843561-1-1.html

86.
rocess vs Threads 区别
Mutex vs semaphore 区别   Lock applied on a distributed system
TCP vs UDP
Implement a key : value data structure like dictionary
1. 先分配一个list，比方说长度为1000，初始值为sys.maxsize；
2. 调用key的__hash__()函数，然后把哈希值模1000，这个值就是value存储的地址；
3. 存的时候，若有冲突，则用拉链法解决冲突，或者考虑扩充list的大小；
import sys
class D(object):
    def __init__(self):
        self.L = [sys.maxsize for i in range(1000)]
    def setter(self,key,value):
        if self.L[key.__hash__()]==sys.maxsize:
            self.L[key.__hash__()] = value
        else:
            self.L[key.__hash__()] = list([self.L[key.__hash__()]])+ [value]
    def getter(self,key):
        if self.‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌L[key.__hash__()] == sys.maxsize:
            raise ValueError
        else:
            return  self.L[key.__hash__()]
刷题网思留 最后返回的是一个 set

# https://www.1point3acres.com/bbs/thread-843427-1-1.html


87.
一共6轮：
1。lunch ambassador
2. craft excellence
3. SD: design calender
4.coding 1: BST search，insert, delete，刷题网上都有
5.HM BQ
6. coding2:
非刷题网题？一个grid，有 0 和 1， 1代表火，0代表没有火。一个人灭火，每次灭火的时候，同一行一列的1都变成0， 求灭火总次数最少的时候的每次灭火位置，一个一个输出。
反馈是coding和design都很好，但是交流不够好，不够senior的bar，down level，没接。感‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌觉小公司出来加上自己英语不够好，很容易被down level。

# https://www.1point3acres.com/bbs/thread-843152-1-1.html

88.
第一轮，聊过去经验，口音看应该是个美国长大的烙印，聊得很行，feedback没问题。
第二轮，三姐，就是432那道全1的题，头一天晚上特意看过，所以code写得很顺利，但是三姐不懂c++。
问了一堆很傻的问题，比如往list里insert一个value，为什么不去连prev和next，
我告诉她这已经builtin了。然后还要一行行的解释code干什么。我在写的时候已经解释过逻辑是什么样的了。
最后相信列出了各种testcases。反馈是这轮struggled，真jb扯蛋，是三姐struggle understand c++ code吧。
给recruiter回信中complain了这货。我面试fail了就算是有被黑也一般就算了，反正于事无补，这次觉得完全是放屁一样的feedback，必须说明一下。
第三轮美国人设计rate limiter，没问题。
第四轮印度老头craftsmanship，聊了不少，结果反馈不佳，这是没地说理去了。他怎么说就怎么是了吧。
第五轮三哥，word ladder和insert interval，这人不错，最后聊了一会天。‍‍‌‍‌‍‌‌‌‌‌‌‌‍‍‌‌
# https://www.1point3acres.com/bbs/thread-843111-1-1.html

89.
领英的面试总体感觉还是很chill的，上来先问一下基础知识，进程和线程的差别，transaction是什么，java的exception
然后题目就一题 利口 而六一

# https://www.1point3acres.com/bbs/thread-843097-1-1.html

90.
infra track电面包含一些操作系统基础知识。What is virtual memory & what is cache。
电面 中国小姐姐 看起来很聪明的样子 给一个graph判断是不是 木又寸。

第一轮系统设计 🇮🇳大哥 放上youtube教程链接
第二轮concurrency 欧洲大哥 经典delay scheduler。这轮感觉像是开卷考试。之前自己尝试用Python模仿一个DelayQueue。
但是因为实在没什么concurrency经验，实现过程中被抠了一个细节，不过整体上框架写出来了。
第三轮coding ABC小哥+🇮🇳shadow大姐 出了一系列简单的题。基本都是十分钟说思路+秒。
从简单双指针到DP到快慢指针到利口 而要，邀遛灵，而遛吴。ABC小哥长得挺帅，VO聊天背景还是塞尔达。
第二天第一轮coding 🇮🇳大哥。李寇遛吴武。但是没有给每一层的推导公式。我在线推导公式但是没来得及推出来，
只能写出BFS框架然后作罢。个人感觉现场推这个公式不是我的强项，暗示了大哥很多次，我说我知道这里面一定有一些relationship，
能不能给点hint。大哥给的hint不知所云，有点尴尬。事后搜索这个题的题干，恍然大悟～
第二天第二轮lunch talk 弯曲土著老爷爷。老爷爷说想问什么问什么，不局限于工作。我当时有点受够了模板问题，
就跟大爷聊了一些弯曲的房价风云变幻/Linkedin的食堂等等问题。大爷说Oh I never expect that。
还跟大爷聊了养狗/生娃当爸爸的焦虑等问题。整体来说聊的很开心，如果当时有lunch吃就更完美了
第二天第三轮BQ 中国小姐姐manager。经典最challenge的project/怎么take feedback。随后小姐姐再次把第一轮system design的问题拿出来talk了一番（应该组里就是做这个的）。

# https://www.1point3acres.com/bbs/thread-842768-1-1.html

91.
店面是个非常nice的国人姐姐
武留凌
伞伞六，follow up 要求写DFS/BFS
# https://www.1point3acres.com/bbs/thread-842748-1-1.html






"""













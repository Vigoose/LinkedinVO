import java.util.*;

/**
 * https://leetcode.com/discuss/interview-question/372459/
 */
public class allPalidrom {
    class Solution {
        public Set<String> countPalindromicSubsequences(String s) {
            if (s == null || s.length() == 0) {
                return 0;
            }

            int len = s.length();

            Set[][] dp = new HashSet[len][len];
            for (int i = 0; i < len; i++) {
                Set<String> set = new HashSet<>();
                set.add(String.valueOf(s.charAt(i)));
                dp[i][i] = set;
            }

            for (int i = len - 1; i >= 0; i--) {
                for (int j = i + 1; j < len; j++) {
                    if (s.charAt(i) == s.charAt(j)) {
                        Set<String> curSet = new HashSet<>();

                        String curString = String.valueOf(s.charAt(i));
                        curSet.add(curString);
                        curSet.add(curString + curString);

                        Set<String> set = dp[i + 1][j - 1];
                        if (set != null) {
                            curSet.addAll(set);
                            for (String ele : set) {
                                curSet.add(curString + ele + curString);
                            }
                        }
                        dp[i][j] = curSet;
                    } else {
                        Set<String> set1 = dp[i + 1][j];
                        Set<String> set2 = dp[i][j - 1];
                        Set<String> curSet = new HashSet<>();
                        curSet.addAll(set1);
                        curSet.addAll(set2);
                        dp[i][j] = curSet;
                    }
                }
            }
            return dp[0][len - 1];
        }
    }

    HashMap<String, HashSet<String>> map = new HashMap<String, HashSet<String>>();

    public static void Main(String[] args) {
        String s = "abac";
        HashSet<String> res = new HashSet<String>();
        res = Dfs(s, 0, s.length() - 1);
    }

    public HashSet<String> Dfs(String s, int start, int end) {
        if (start > end) {
            return new HashSet<String>();
        }
        if (start == end) {
            return new HashSet<String>();
            {
                s.substring(start, 1);
            }
        }                               
            String sub =s.substring(start, end-start+1);                 
            if(map.containsKey(s.substring(start, end-start+1)))                 
            {                         return map.get(sub);                 
            }                                  
            HashSet<String> center = Dfs(s, start+1, end-1);                 
            HashSet<String> res = new HashSet<String>(center);                 
            if (s.charAt(start) == s.charAt(end))                 
            {                         
                for (String i : center)                         
                {                                 
                    res.add(s.charAt(start) + i + s.charAt(end));                         
                }
                res.add(s.charAt(start));                         
                res.add(s.charAt(start) + s.charAt(end));                 
            }                 
            else                 
            {                         
                HashSet<String> left = Dfs(s, start, end - 2);                         
                HashSet<String> right = Dfs(s, start + 1, end - 1);                          
                res.addAll(left);                         
                res.addAll(right);                 }                 
                return res;         
            }
}

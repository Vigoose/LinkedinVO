import java.util.*;

public class ksum {
    interface IKSum {

        List<List<Integer>> kSum(int nums[], int k, int target);
    }

    /**
     * We'll use the problem of k sum and reduce it to two sum and attache the
     * result back
     */
    class KSumSorting implements IKSum {

        @Override
        public List<List<Integer>> kSum(int[] nums, int k, int target) {
            if (nums == null || nums.length == 0 || nums.length < k)
                return Collections.EMPTY_LIST;

            Arrays.sort(nums);

            return kSum(nums, k, 0, target);

        }

        private List<List<Integer>> kSum(int[] nums, int k, int start, int target) {
            int len = nums.length;
            List<List<Integer>> result = new ArrayList<>();
            if (len < k)
                return Collections.EMPTY_LIST;

            if (k == 2) {
                return twoSum(nums, start, len - 1, target);
            } else {

                /**
                 * Take each element, and exclude it from target to reduce the problem to
                 * smaller k-1 sum problem
                 */
                for (int i = start; i < len - (k - 1); i++) {
                    /**
                     * Avoid duplicates
                     */
                    if (i > start && nums[i] == nums[i - 1])
                        continue;

                    int ele = nums[i];

                    int rem = target - nums[i];
                    List<List<Integer>> smallerSumResult = kSum(nums, k - 1, i + 1, rem);

                    /**
                     * Append the current element to make it k sum from k-1 sum
                     */
                    for (List<Integer> list : smallerSumResult)
                        list.add(0, ele);

                    /**
                     * Append to our result
                     */
                    result.addAll(smallerSumResult);

                }
            }

            return result;
        }

        private List<List<Integer>> twoSum(int nums[], int low, int high, int target) {

            List<List<Integer>> result = new ArrayList<>();

            while (low < high) {

                int sum = nums[low] + nums[high];

                if (sum == target) {
                    List<Integer> twoSum = new ArrayList<>();
                    twoSum.add(nums[low]);
                    twoSum.add(nums[high]);

                    result.add(twoSum);

                    /**
                     * Avoid duplicates
                     */

                    while (low < high && nums[low] == nums[low + 1])
                        low++;
                    while (high > low && nums[high] == nums[high - 1])
                        high--;

                } else if (sum < target)
                    low++;
                else
                    high--;

            }

            return result;
        }
    }
}

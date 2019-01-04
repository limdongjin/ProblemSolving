import java.util.Hashtable;

class Solution5 {
    public int[] twoSum(int[] nums, int target) {
        int nums_length = nums.length;
        Hashtable<Integer, Integer> hashtable = new Hashtable<>();
        Integer dup;
        int i;
        for(i = 0; i < nums_length; ++i){
            dup = hashtable.get(nums[i]);
            if(dup != null && nums[i]*2 == target){
                // ex, nums = {0, 4, 3, 0}, target = 0
                return new int[]{dup, i};
            }
            Integer resIdx = hashtable.get(target - nums[i]);
            if(resIdx != null){
                return new int[]{resIdx, i};
            }
            hashtable.put(nums[i], i);
        }
        return new int[]{1, 2};
    }
    // Runtime: 8 ms, faster than 56.04% of Java online submissions for Two Sum.
}
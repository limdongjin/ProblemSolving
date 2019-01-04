import java.util.HashMap;

class Solution4 {
    public int[] twoSum(int[] nums, int target) {
        int nums_length = nums.length;
        HashMap<Integer, Integer> hashMap = new HashMap<>(); // <value, index>
        Integer dup;
        int i;
        for(i = 0; i < nums_length; ++i){
            dup = hashMap.get(nums[i]);
            if(dup != null && nums[i]*2 == target){
                // ex, nums = {0, 4, 3, 0}, target = 0
                return new int[]{dup, i};
            }
            Integer resIdx = hashMap.get(target - nums[i]);
            if(resIdx != null){
                return new int[]{resIdx, i};
            }
            hashMap.put(nums[i], i);
        }
        return new int[]{1, 2};
    }
    // Runtime: 8 ms, faster than 56.04% of Java online submissions for Two Sum.
}
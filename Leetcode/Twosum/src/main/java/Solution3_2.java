import java.util.HashMap;

class Solution3_2 {
    public int[] twoSum(int[] nums, int target) {
        int nums_length = nums.length;
        HashMap<Integer, Integer> hashMap = new HashMap<>(); // <value, index>
        Integer dup, resIdx;
        for(int i = 0; i < nums_length; ++i){
            dup = hashMap.get(nums[i]);
            if(dup != null && nums[i]*2 == target){
                // ex, nums = {0, 4, 3, 0}, target = 0
                return new int[]{dup, i};
            }
            hashMap.put(nums[i], i);
        }
        for(int j = 0; j < nums_length; ++j){
            resIdx = hashMap.get(target - nums[j]);
            if(resIdx != null && resIdx != j){
                return new int[]{j, resIdx};
            }
        }
        return new int[]{1, 2};
    }
    // Runtime: 9 ms, faster than 49.62%  of Java online submissions for Two Sum.
}
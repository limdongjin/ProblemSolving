import java.util.HashMap;

class Solution7 {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int nums_length = nums.length;
        for(int i=0;i<nums_length;i++){
            Integer res = map.get(nums[i]);
            if(res != null){
                return new int[]{res, i};
            }else{
                map.put(target - nums[i], i);
            }
        }
        return new int[]{1,2};
    }
    // Runtime: 6 ms, faster than 72.77% of Java online submissions for Two Sum.
}
import java.util.ArrayList;
import java.util.List;

class Solution6 {
    public int[] twoSum(int[] nums, int target) {
        int i, resIdx;
        int nums_length = nums.length;
        List<Integer> arrayListNums = new ArrayList<>();
        for(final int num : nums){
            arrayListNums.add(num);
        }
        for(i=0;i<nums_length;++i){
            resIdx = arrayListNums.lastIndexOf(target - nums[i]);
            if(resIdx != -1 && resIdx != i){
                System.out.println(resIdx);
                return new int[]{i, resIdx};
            }
        }
        return new int[]{1, 2};
    }
    // Runtime: 125 ms, faster than 2.39% of Java online submissions for Two Sum.
}
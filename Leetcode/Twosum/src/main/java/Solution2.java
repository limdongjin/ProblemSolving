import java.util.Arrays;

class Solution2 {
    /**
     * @param array of integers
     * @param target
     * @return indices of the two numbers such that they add up to a specific target.
     */
    public int[] twoSum(int[] nums, int target) {
        int nums_length  = nums.length;
        for(int i = 0; i < nums_length - 1; ++i){
            int resIdx = indexOf(Arrays.copyOfRange(nums, i + 1, nums_length), target - nums[i]);
            if(resIdx != -1){
                return new int[]{i, resIdx + i + 1};
            }
        }
//        System.out.println();

        return new int[]{0, 1};
    }



    private int indexOf(int[] nums, int target){
        int nums_length = nums.length;
        for(int i = 0; i < nums_length; ++i){
            if(nums[i] == target){
                return i;
            }
        }
        return -1;
    }

    // Runtime: 77 ms, faster than 7.31% of Java online submissions for Two Sum.
}

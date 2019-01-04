class Solution1{
    /**
     * @param array of integers
     * @param target
     * @return indices of the two numbers such that they add up to a specific target.
     */
    public int[] twoSum(int[] nums, int target) {
        int nums_length  = nums.length;
        for(int i=0; i < nums_length - 1; ++i){
            for(int j=i+1; j < nums_length; ++j){
                if(nums[j] == target - nums[i]){
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{0, 1};
    }
    // Runtime: 47 ms, faster than 15.54% of Java online submissions for Two Sum.
}
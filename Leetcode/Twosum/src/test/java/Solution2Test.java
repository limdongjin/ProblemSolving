import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class Solution2Test {
    private Solution2 solution2 = new Solution2();

    @Before
    public void setUp() {
//        System.out.printf("h");
        solution2 = new Solution2();
    }

    @Test
    public void twoSum() {
        assertArrayEquals(new int[]{0, 1}, solution2.twoSum(new int[]{2, 7, 11, 15}, 9));
    }

    @Test
    public void twoSum1(){
        assertArrayEquals(new int[]{1, 2}, solution2.twoSum(new int[]{2, 10, 20, 1}, 30));
    }

    @Test
    public void twoSum2(){
        assertArrayEquals(new int[]{1, 2}, solution2.twoSum(new int[]{3,2,4}, 6));
    }
}
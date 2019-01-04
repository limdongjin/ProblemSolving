import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class Solution1Test {
    private Solution1 solution1;

    @Before
    public void setUp() {
        solution1 = new Solution1();
    }

    @Test
    public void twoSum() {
        assertArrayEquals(new int[]{0, 1}, solution1.twoSum(new int[]{2, 7, 11, 15}, 9));
    }

    @Test
    public void twoSum1(){
        assertArrayEquals(new int[]{1, 2}, solution1.twoSum(new int[]{2, 10, 20, 1}, 30));
    }

    @Test
    public void twoSum2(){
        assertArrayEquals(new int[]{1, 2}, solution1.twoSum(new int[]{3,2,4}, 6));
    }
    @Test
    public void twoSum3(){
        assertArrayEquals(new int[]{0, 3}, solution1.twoSum(new int[]{0, 4, 3, 0}, 0));
    }
}
import org.junit.Before;
import org.junit.Test;

import java.util.Arrays;
import java.util.HashMap;

import static org.junit.Assert.*;

public class Solution3Test {
    private Solution3 solution3;
    @Before
    public void setUp() {
        solution3 = new Solution3();
    }
    @Test
    public void foo(){
        System.out.printf("foo : %d\n", Arrays.binarySearch(new int[]{0, 3, 4, 0}, 1, 4, 0));
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        hashMap.put(1, 1);
        System.out.println(hashMap.get(0));
    }

    @Test
    public void twoSum() {
        assertArrayEquals(new int[]{0, 1}, solution3.twoSum(new int[]{2, 7, 11, 15}, 9));
    }

    @Test
    public void twoSum1(){
        assertArrayEquals(new int[]{1, 2}, solution3.twoSum(new int[]{2, 10, 20, 1}, 30));
    }

    @Test
    public void twoSum2(){
        assertArrayEquals(new int[]{1, 2}, solution3.twoSum(new int[]{3,2,4}, 6));
    }

    @Test
    public void twoSum3(){
        assertArrayEquals(new int[]{0, 3}, solution3.twoSum(new int[]{0, 4, 3, 0}, 0));
    }
}
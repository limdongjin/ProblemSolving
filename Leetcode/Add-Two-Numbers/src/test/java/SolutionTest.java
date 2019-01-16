import org.junit.Before;
import org.junit.Test;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import static org.junit.Assert.*;

public class SolutionTest {
    private ListNode l1;
    private ListNode l2;

    private ListNode bl1;
    private ListNode bl2;

    private ListNode toobl1;
    private ListNode toobl2;

    private List expected1;
    private List expected2;
    private List expected3;

    private Solution solution;

    @Before
    public void setUp(){
        solution = new Solution();

        l1 = ListNode.makeLinkedList(new int[]{2, 4, 3});
        l2 = ListNode.makeLinkedList(new int[]{5, 6, 4});
        expected1 = Arrays.stream(new Integer[]{7, 0, 8}).collect(Collectors.toList());

        bl1 = ListNode.makeLinkedList(new int[]{ 9 });
        bl2 = ListNode.makeLinkedList(new int[]{1,9,9,9,9,9,9,9,9,9});
        expected2 = Arrays.stream(new Integer[]{0,0,0,0,0,0,0,0,0,0,1}).collect(Collectors.toList());

        toobl1 = ListNode.makeLinkedList(new int[]{1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1});
        toobl2 = ListNode.makeLinkedList(new int[]{5, 6, 4});
        expected3 = Arrays.stream(new Integer[]{6,6,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1}).collect(Collectors.toList());
    }

    @Test
    public void 기본예제_l1_l2_테스트() {
        ListNode l = solution.addTwoNumbers(l1, l2);
        assertEquals(ListNode.linkedListToList(l), expected1);
    }

    @Test
    public void bl1_bl2_테스트(){
        ListNode l = solution.addTwoNumbers(bl1, bl2);

        assertEquals(ListNode.linkedListToList(l), expected2);
    }

    @Test
    public void 매우매우매우큰_링크드리스트_테스트(){
        ListNode l = solution.addTwoNumbers(toobl1, toobl2);

        assertEquals(ListNode.linkedListToList(l), expected3);
    }
}
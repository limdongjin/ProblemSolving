
public class WrongSolution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return longToLinkedList(linkedListToLong(l1) + linkedListToLong(l2));
    }

    private static long linkedListToLong(ListNode linkedList){
        ListNode point = linkedList;
        long res = point.val;
        long weight = 10;

        while (point.next != null){
            res += point.next.val * weight;
            point = point.next;
            weight *= 10;
        }
        return res;
    }

    private static ListNode longToLinkedList(long value){
        ListNode res = new ListNode((int)(value % 10));
        ListNode point = res;
        ListNode next;
        value /= 10;

        while (value != 0){
            next = new ListNode((int)(value % 10));
            value /= 10;
            point.next = next;
            point = next;
        }
        return res;
    }
}
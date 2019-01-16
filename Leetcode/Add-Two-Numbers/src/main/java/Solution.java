public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode point1 = l1;
        ListNode point2 = l2;
        ListNode point3;

        ListNode res;
        ListNode node;

        int sum;
        int carry = 0;

        sum = sumNode(point1, point2);

//        if(sum >= 10){
//            sum -= 10;
//            carry = 1;
//        }

        carry = sum / 10;
        sum = sum % 10;

        res = new ListNode(sum);

        point1 = point1.next;
        point2 = point2.next;
        point3 = res;

        while (point1 != null || point2 != null){

            sum = sumNode(point1, point2);
            sum += carry;

//            carry = 0;
//            if(sum >= 10) {
//                sum -= 10;
//                carry = 1;
//            }

            carry = sum / 10;
            sum = sum % 10;

            node = new ListNode(sum);

            point3.next = node;
            point3 = node;

            if(point1 != null) point1 = point1.next;
            if(point2 != null) point2 = point2.next;
        }

        if(carry != 0){
            point3.next = new ListNode(1);
        }

        return res;
    }

    private static int sumNode(ListNode point1, ListNode point2){
        int sum = 0;
        if(point1 != null) sum += point1.val;
        if(point2 != null) sum += point2.val;
        return sum;
    }
    // Runtime: 44 ms, faster than 39.03% of Java online submissions for Add Two Numbers.
}
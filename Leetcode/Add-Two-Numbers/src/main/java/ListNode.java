import java.util.ArrayList;
import java.util.List;

public class ListNode {
    final int val;
    ListNode next;

    ListNode(int x) { val = x; }

    public static ListNode makeLinkedList(int[] elements){
        ListNode res = new ListNode(elements[0]);
        ListNode nextNode;
        ListNode point = res;

        for(int i = 1; i < elements.length; ++i) {
            nextNode = new ListNode(elements[i]);
            point.next = nextNode;
            point = nextNode;
        }

        return res;
    }

   public static void printLinkedList(ListNode linkedList){
        ListNode point;
        point = linkedList;

        System.out.print(point.val);
        while (point.next != null) {
            System.out.print(" -> ");
            point = point.next;
            System.out.print(point.val);
        }
        System.out.println("\n");
   }

   public static List linkedListToList(ListNode linkedList){
       ListNode point;
       List<Integer> res = new ArrayList();

       point = linkedList;
       res.add(point.val);
       while (point.next != null){
           point = point.next;
           res.add(point.val);
       }
       return res;
    }
}
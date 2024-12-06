/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int pairSum(ListNode head) {
        // Find middle of linked list using fast-slow pointer
        // Reverse 2nd half
        // Create another fast pointer n/2 ahead of slow. Iterate n/2
        // times from head to find every pair sum.


        var fast = head.next;
        var mid = head;
        int ans = 0;

        // length 2
        if (fast.next == null){
            return fast.val + head.val;
        }

        while (fast != null && fast.next != null){
            fast = fast.next.next;
            mid = mid.next;
        }

        ListNode prev = null;
        mid = mid.next;

        while (mid != null){
            var next = mid.next;
            mid.next = prev;
            prev = mid;
            mid = next;
        }

        while (prev != null){
            ans = Math.max(ans, head.val + prev.val);
            head = head.next;
            prev = prev.next;
        }

        return ans;

    }
}
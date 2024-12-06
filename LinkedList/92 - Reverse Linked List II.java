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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        // identify borders:
        if (head.next == null || left == right){
            return head;
        }
        var dummy = new ListNode(0,head);

        // 1) find left
        var leftN = dummy;
        var curr = head;
        for (int i =0; i<left-1;i++){
            leftN = leftN.next;
            curr = curr.next;
        }
        // now leftN = node before left, curr = begin of reverse section


        ListNode prev = null;
        // 2)reverse mid
        for(int i = 0; i < right-left+1; i++){
            var nextNode = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextNode;
        }
        // curr now = R.next, p = begin of the reversed list

        // 3) link
        var lastNodeReversed = leftN.next;
        leftN.next = prev; // L.prev linked to begin of rev list
        lastNodeReversed.next = curr; // last rev node linked to R.next

        return dummy.next;
    }
}
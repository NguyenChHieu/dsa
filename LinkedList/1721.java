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
    public ListNode swapNodes(ListNode head, int k) {
        ListNode l = null;
        ListNode r = null;
        ListNode temp  = head;
        while(temp != null){

            if (r != null){ // now temp is k-th node away from the head, so when it reaches the end, r will be k node away from end
                r = r.next;
            }

            k--;
            if (k == 0){
                l = temp;
                r = head;
            }
            temp = temp.next;
        }

        int tempVal = l.val;
        l.val = r.val;
        r.val = tempVal;
        return head;
    }
}
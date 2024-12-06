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
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null){
            return head;
        }

        var dummy = new ListNode(-101);
        dummy.next = head;
        var curr = dummy;

        while (curr.next != null && curr.next.next != null){
            if (curr.next.val != curr.next.next.val){
                curr = curr.next;
            }
            else{
                var runNode = curr.next;
                int dupVal = runNode.val;
                // run thru all dup values before assign current's pointer to another non-duplicated node
                while (runNode != null && runNode.val == dupVal){
                    runNode = runNode.next;
                }

                // RunNode now is a new non-duplicated Node after traversing thru the dups sequence in the while loop
                curr.next = runNode;
            }
        }
        return dummy.next;

    }
}
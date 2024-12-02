class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0, head);
        var prev = dummy;
        var curr = head;

        while (curr != null && curr.next != null){
            var nextNode = curr.next.next;
            prev.next = curr.next;
            curr.next.next = curr;
            curr.next = nextNode;
            prev = curr;
            curr = nextNode;
        }
        return dummy.next;
    }
}
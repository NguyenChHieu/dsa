class MyLinkedList {
    private LinkedListN head;

    public MyLinkedList() {
    }

    public int get(int index) {
        // empty list/invalid index
        if (head==null || index < 0){
            return -1;
        }

        // valid case
        int curr = 0;
        LinkedListN currN = head;
        while (currN != null){
            if (curr == index){
                return currN.val;
            }
            currN = currN.next;
            curr++;
        }
        // index not found
        return -1;
    }

    public void addAtHead(int val) {
        LinkedListN newHead = new LinkedListN(val, head);
        this.head = newHead;
    }

    public void addAtTail(int val) {
        // add as a head
        if (head==null){
            LinkedListN newHead = new LinkedListN(val, null);
            this.head = newHead;
            return;
        }

        // normal case
        LinkedListN curr = head;
        LinkedListN newNode = new LinkedListN(val, null);
        while (curr.next != null){
            curr = curr.next;
        }
        curr.next = newNode;
    }


    public void addAtIndex(int index, int val) {
        // invalid index
        if (index < 0){
            return;
        }

        // add new head
        if (index == 0){
            LinkedListN newNode = new LinkedListN(val, head);
            this.head = newNode;
            return;
        }

        // empty list
        if (head == null){
            return;
        }

        // normal case
        LinkedListN curr = head;
        while (index-1 >0){
            if (curr.next == null){
                return;
            }
            index--;
            curr = curr.next;
        }

        LinkedListN newNode = new LinkedListN(val, curr.next);
        curr.next = newNode;
    }

    public void deleteAtIndex(int index) {
        if (index < 0){
            return;
        }

        if (head == null){
            return;
        }

        if (index == 0){
            this.head = head.next;
            return;
        }

        LinkedListN curr = head;
        while (index-1 >0){
            if (curr == null){
                return;
            }
            index--;
            curr = curr.next;
        }
        if (curr != null && curr.next != null){
            curr.next = curr.next.next;
        }
    }
}

class LinkedListN{
    protected LinkedListN next;
    protected int val;

    public LinkedListN(int val, LinkedListN next){
        this.next = next;
        this.val = val;
    }
}


/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) {
        MyStack obj = new MyStack();
        obj.push(1);
        obj.push(2);
        obj.push(3);
        obj.pop();
        obj.pop();
        System.out.println(obj.top());

    }
}

// 2 stack approach
class MyStack {

    private Queue<Integer> fst = new LinkedList<>();
    private Queue<Integer> sec = new LinkedList<>();

    public MyStack() {
    }

    public void push(int x) {
        if (fst.isEmpty()){
            fst.offer(x);
        }
        else{
            int num = fst.poll();
            sec.offer(num);
            fst.offer(x);
        }
    }

    public int pop() {
        if (!fst.isEmpty()){
            int ret = fst.poll();
            // more than 1 ele in this DSS
            if (!sec.isEmpty()){
                while (sec.size() != 1){
                    fst.offer(sec.poll());
                }
                int newTop = sec.poll();
                while (!fst.isEmpty()){
                    sec.offer(fst.poll());
                }
                fst.offer(newTop);
                // else, there's only 1 element and it was popped
            }
            return ret;
        }
        return -1;
    }

    public int top() {
        if (!fst.isEmpty()){
            return fst.peek();
        }
        return -1;
    }

    public boolean empty() {
        return fst.isEmpty() && sec.isEmpty();
    }
}

// 1 stack approach
class MyStack {
    private Queue<Integer> queue;

    public MyStack() {
        queue=new LinkedList<>();

    }

    public void push(int x) {
        queue.offer(x);
        for(int i=0;i<queue.size()-1;i++){
            queue.offer(queue.poll());
        }

    }

    public int pop() {
        return queue.remove();

    }

    public int top() {
        return queue.peek();

    }

    public boolean empty() {
        return queue.isEmpty();

    }
}
class MinStack {

    private Stack<StackNumber> st = new Stack<>();

    public MinStack() {
    }

    public void push(int val) {
        var num = new StackNumber(val,null);

        if (st.isEmpty()){
            num.currMin = num.val;
            st.push(num);
        }
        else{
            var top = st.peek();
            if (top.currMin > val)
                num.currMin = num.val;
            else num.currMin = top.currMin;
            st.push(num);
        }
    }

    public void pop() {
        st.pop();
    }

    public int top() {
        return st.peek().val;
    }

    public int getMin() {
        return st.peek().currMin;
    }
}

class StackNumber {
    public int val;
    public Integer currMin;

    public StackNumber (int val, Integer currMin){
        this.val = val;
        this.currMin = currMin;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
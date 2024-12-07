import java.util.*;

public class Main {
    public static void main(String[] args) {
//        System.out.println(validateStackSequences(new int[]{1, 2, 3, 4, 5}, new int[]{4, 5, 3, 2, 1}));
//        System.out.println(validateStackSequences(new int[]{1, 2, 3, 4, 5}, new int[]{4, 3, 5, 1, 2}));
//        System.out.println(validateStackSequences(new int[]{1, 2, 3, 4, 5}, new int[]{6,7,7,8,9}));
        System.out.println(validateStackSequences(new int[]{1,2,3,5,4}, new int[]{1,2,4,3,5}));
    }

    //    public static boolean validateStackSequences(int[] pushed, int[] popped) {
//        Stack<Integer> st = new Stack<>();
//
//        int i = 0;
//        int k = 0;
//        while (i < pushed.length && k < popped.length) {
//            if (pushed[i] != popped[k]) {
//                st.push(pushed[i]);
//                i++;
//            } else {
//                i++;
//                k++;
//                if (st.isEmpty()) {
//                    continue;
//                }
//                while (st.peek() == popped[k]) {
//                    st.pop();
//                    k++;
//                    if (st.isEmpty()) {
//                        break;
//                    }
//                }
//            }
//        }
//        return st.isEmpty();
//    }
    public static boolean validateStackSequences(int[] pushed, int[] popped) {
        int pushI = 0, popI = 0;

        for (int num : pushed) {
            pushed[pushI] = num;
            pushI++;
            while (pushI > 0 && pushed[pushI - 1] == popped[popI]) {
                popI++;
                pushI--;
            }
        }
        return pushI == 0;
    }
}


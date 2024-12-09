import java.util.*;

public class Main {
    public static void main(String[] args) {
        System.out.println(robotWithString("mmuqezwmomeplrtskz"));
    }



    public static String robotWithString(String s) {
        char[] arr = s.toCharArray();
        int n = arr.length;
        // array store idx of smallest character in the suffix from each position
        int[] rightMin = new int[n];
        rightMin[n - 1] = n-1;

        for (int i = n - 2; i >= 0; i--) {
            rightMin[i] = arr[i] <= arr[rightMin[i + 1]] ? i : rightMin[i + 1];
        }

        var ans = new StringBuilder();
        var st = new StringBuilder();

        int start = 0;
        while (start < n){

            // get the idx of the smallest character in the suffix
            int minIdx = rightMin[start];
            // C1: top stack <= smallest character in the suffix
            // --> pop the top stack and append to the result since
            // its lexi <= all remaining chars
            if (!st.isEmpty()
                    && st.charAt(st.length()-1) <= arr[minIdx]) {
                ans.append(st.charAt(st.length()-1));
                st.deleteCharAt(st.length()-1);
            }
            // C2: top stack > smallest character in the suffix
            // --> append the smallest character in the suffix to the result
            // and append the remaining suffix to the stack
            else{
                ans.append(arr[minIdx]);
                // push the substring from i to minIdx to the stack - these will be processed later
                st.append(s, start, minIdx);
                // update the range from prev I to the next smallest character
                // eg: "bac" --> "b" > "a" --> i becomes 1 + 1 = 2
                start = minIdx + 1;
            }
        }

        ans.append(st.reverse());
        return ans.toString();
    }
}
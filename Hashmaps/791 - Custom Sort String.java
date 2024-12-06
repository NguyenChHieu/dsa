class Solution {
    public String customSortString(String order, String s) {
        HashMap<Character, Integer> org = new HashMap<>();

        /* count the freq of characters in s that appear in
        order. Since the order of other characters does not matter,
        then just count their freq too.
        */

        for (char ch: s.toCharArray()){
            org.put(ch, org.getOrDefault(ch,0)+1);
        }

        StringBuilder sb = new StringBuilder();

        for (char ch: order.toCharArray()){
            if (org.containsKey(ch)){
                for (int i = 0; i< org.get(ch);i++){
                    sb.append(ch);
                }
                org.remove(ch);
            }
        }

        if (org.isEmpty()){
            return sb.toString();
        }

        for (char ch: org.keySet()){
            for (int i = 0; i< org.get(ch);i++){
                sb.append(ch);
            }
        }

        return sb.toString();
    }
}
class Solution {
    public boolean closeStrings(String word1, String word2) {
        if (word1.length() != word2.length()){
            return false;
        }

        HashMap<Character, Integer> save = new HashMap<>();
        HashMap<Character, Integer> save1 = new HashMap<>();

        for(int i = 0; i < word1.length(); i ++){
            save.put(word1.charAt(i), save.getOrDefault(word1.charAt(i), 0)+1);
        }

        for(int i = 0; i < word1.length(); i ++){
            save1.put(word2.charAt(i), save1.getOrDefault(word2.charAt(i), 0)+1);
        }

        if (!save.keySet().equals(save1.keySet())){
            return false;
        }

        var values = new ArrayList<>(save.values());
        var values1 = new ArrayList<>(save1.values());
        Collections.sort(values);
        Collections.sort(values1);

        return values.equals(values1);
    }
}
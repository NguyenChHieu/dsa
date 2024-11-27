class Solution {
    public boolean checkInclusion(String s1, String s2) {

        if (s2.length() < s1.length()){
            return false;
        }

        int[] org = new int[26];
        int[] save = new int[26];

        for (Character chara : s1.toCharArray()){
            org[chara-'a']++;
        }

        int l = 0;
        int r = 0;
        while (r < s2.length()){
            var c = s2.charAt(r);
            save[c-'a']++;

            while (r - l + 1 > s1.length()){
                save[s2.charAt(l) - 'a']--;
                l++;
            }

            if (match(org, save)){
                return true;
            }
            r++;

        }
        return false;

    }

    private boolean match(int[] S1, int[] S2){
        for (int i = 0; i < S1.length; i++){
            if (S1[i] != S2[i]){
                return false;
            }
        }
        return true;
    }
}
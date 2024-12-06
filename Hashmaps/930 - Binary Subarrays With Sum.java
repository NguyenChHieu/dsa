class Solution {
    // similar to 560
    public int numSubarraysWithSum(int[] nums, int goal) {
        HashMap<Integer, Integer> save = new HashMap<>();
        save.put(0,1);

        int curr = 0;
        int ans = 0;

        for (int num: nums){
            curr += num;
            if (save.containsKey(curr - goal)){
                ans += save.get(curr-goal);
            }

            save.put(curr, save.getOrDefault(curr,0) + 1);
        }
        return ans;
    }
}